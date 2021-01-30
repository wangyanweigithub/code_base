#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "LRUImpl.h"

static void freeList(LRUCache *cache);

static cacheEntry* newCacheEntry(char key, char data) {
	cacheEntry* entry = NULL;
	if (NULL == (entry=malloc(sizeof(*entry)))) {
		perror("malloc");
		return NULL;
	}
	memset(entry, 0, sizeof(*entry));
	entry->key = key;
	entry->data = data;
	return entry;
}

static void freeCacheEntry(cacheEntry* entry) {
	if (NULL == entry) return;
	free(entry);
}

int LRUCacheCreate(int capacity, void **lruCache) {
	LRUCache* cache = NULL;
	if (NULL == (entry=malloc(sizeof(*entry))))
}
