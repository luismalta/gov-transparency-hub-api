def _extract_pagination(filters: dict) -> dict:
    pagination_info = {"page": 0, "page_size": 100}

    if "page" in filters:
        pagination_info["page"] = filters.pop("page")
    if "page_size" in filters:
        pagination_info["page_size"] = filters.pop("page_size")

    return pagination_info, filters
