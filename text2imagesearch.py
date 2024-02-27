import typing as t

import qdrant_client as qc
import torch
import transformers

import qdrant_client.models


# Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0]  # First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


class Text2ImageSearch:
    def __init__(self, qdrant_url: str, qdrant_collection: str):
        embedding_model_name = 'sentence-transformers/all-MiniLM-L6-v2'
        self.embedding_tokenizer = transformers.AutoTokenizer.from_pretrained(embedding_model_name)
        self.embedding_model = transformers.AutoModel.from_pretrained(embedding_model_name)
        self.qdrant = qc.QdrantClient(qdrant_url)
        self.qdrant_collection = qdrant_collection

    def __call__(self, query: str, limit: int, threshold: t.Optional[float] = None) -> t.List[qc.models.ScoredPoint]:
        query_tokens = self.embedding_tokenizer(query.lower(), return_tensors='pt')
        query_embedding = self.embedding_model(**query_tokens)
        query_embedding = mean_pooling(query_embedding, query_tokens['attention_mask'])
        query_embedding = torch.nn.functional.normalize(query_embedding, p=2, dim=1)

        resp = self.qdrant.search(
            collection_name=self.qdrant_collection,
            query_vector=query_embedding.squeeze().cpu().detach().numpy(),
            # with_vectors=True,
            limit=limit,
            score_threshold=threshold
        )
        return resp



