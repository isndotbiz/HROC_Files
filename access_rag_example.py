#!/usr/bin/env python3
"""
Helper class to access fal.ai documentation from RAG system
Hardcoded configuration for easy reuse
"""
import chromadb
from chromadb.config import Settings

class FalAiRAG:
    """Access fal.ai documentation from ChromaDB RAG system"""

    def __init__(self):
        self.config = {
            "chromadb_path": "/home/jdmal/workspace/rag-system/chroma_db",
            "collection_name": "api_providers_docs",
            "source_filter": "fal-ai",
            "top_k": 5
        }

        # Initialize ChromaDB client
        self.client = chromadb.PersistentClient(
            path=self.config["chromadb_path"],
            settings=Settings(anonymized_telemetry=False)
        )

        # Get collection
        self.collection = self.client.get_collection(self.config["collection_name"])

    def query_fal(self, query, top_k=None):
        """
        Query fal.ai documentation

        Args:
            query: Question or search term
            top_k: Number of results (default from config)

        Returns:
            List of dicts with 'document' and 'metadata' keys
        """
        k = top_k or self.config["top_k"]

        results = self.collection.query(
            query_texts=[query],
            n_results=k,
            where={"source": self.config["source_filter"]}
        )

        # Format results
        formatted = []
        for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
            formatted.append({
                'document': doc,
                'metadata': meta
            })

        return formatted

    def search_by_topic(self, topic, top_k=10):
        """Search for specific topics like 'image editing' or 'gpt-image'"""
        return self.query_fal(topic, top_k=top_k)


# Usage example
if __name__ == "__main__":
    rag = FalAiRAG()

    # Example: Find image generation docs
    results = rag.query_fal("How do I generate images with fal.ai?")

    print(f"Found {len(results)} results:\n")
    for i, result in enumerate(results, 1):
        print(f"[{i}] {result['metadata'].get('title', 'No title')}")
        print(f"    {result['document'][:200]}...")
        print()
