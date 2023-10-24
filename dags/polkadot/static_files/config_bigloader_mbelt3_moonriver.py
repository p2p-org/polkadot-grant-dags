from google.cloud import bigquery

# write_disposition - this is for writing data to bigquery
# update_type - this is for taking data by increment from postgres
# 'update_type': 'increment' - if table in bigquery exists only

CHAIN = 'moonriver'
# WRITE_DISPOSITION = 'write_truncate'
WRITE_DISPOSITION = 'append'
# UPDATE_TYPE = 'full'
UPDATE_TYPE = 'increment'

TABLE_CONF = {
    'blocks': {
        'schema': [
            bigquery.SchemaField("network_id", "INT64"),
            bigquery.SchemaField("block_id", "INT64"),
            bigquery.SchemaField("hash", "STRING"),
            bigquery.SchemaField("state_root", "STRING"),
            bigquery.SchemaField("extrinsics_root", "STRING"),
            bigquery.SchemaField("parent_hash", "STRING"),
            bigquery.SchemaField("author", "STRING"),
            bigquery.SchemaField("digest", "STRING"),
            bigquery.SchemaField("block_time", "TIMESTAMP"),
            bigquery.SchemaField("row_id", "INT64"),
            bigquery.SchemaField("metadata", "STRING"),
            bigquery.SchemaField("row_time", "TIMESTAMP"),
        ],
        # 'query_select': 'SELECT * FROM blocks',
        'write_disposition': WRITE_DISPOSITION,
        'id_col_name': 'row_id',
        'update_type': UPDATE_TYPE,
        'file_size_limit_rows': 5_000_000,
    },

    'rounds': {
        'schema': [
            bigquery.SchemaField("network_id", "INT64"),
            bigquery.SchemaField("round_id", "INT64"),
            bigquery.SchemaField("total_stake", "NUMERIC"),
            bigquery.SchemaField("total_reward_points", "INT64"),
            bigquery.SchemaField("total_reward", "NUMERIC"),
            bigquery.SchemaField("collators_count", "INT64"),
            bigquery.SchemaField("start_block_id", "INT64"),
            bigquery.SchemaField("start_block_time", "TIMESTAMP"),
            bigquery.SchemaField("payout_block_id", "INT64"),
            bigquery.SchemaField("payout_block_time", "TIMESTAMP"),
            bigquery.SchemaField("row_id", "INT64"),
            bigquery.SchemaField("runtime", "INT64"),
            bigquery.SchemaField("row_time", "TIMESTAMP"),
        ],
        # 'query_select': 'SELECT * FROM blocks',
        'write_disposition': WRITE_DISPOSITION,
        'id_col_name': 'row_id',
        'update_type': UPDATE_TYPE,
        'file_size_limit_rows': 5_000_000,
    },

     'stake_rounds': {
        'schema': [
            bigquery.SchemaField("network_id", "INT64"),
            bigquery.SchemaField("round_id", "INT64"),
            bigquery.SchemaField("total_stake", "NUMERIC"),
            bigquery.SchemaField("collators_count", "INT64"),
            bigquery.SchemaField("start_block_id", "INT64"),
            bigquery.SchemaField("start_block_time", "TIMESTAMP"),
            bigquery.SchemaField("row_id", "INT64"),
            bigquery.SchemaField("row_time", "TIMESTAMP"),
        ],
        # 'query_select': 'SELECT * FROM blocks',
        'write_disposition': WRITE_DISPOSITION,
        'id_col_name': 'row_id',
        'update_type': UPDATE_TYPE,
        'file_size_limit_rows': 5_000_000,
    },

    'rewards_rounds': {
        'schema': [
            bigquery.SchemaField("network_id", "INT64"),
            bigquery.SchemaField("round_id", "INT64"),
            bigquery.SchemaField("total_reward_points", "INT64"),
            bigquery.SchemaField("total_reward", "NUMERIC"),
            bigquery.SchemaField("payout_block_id", "INT64"),
            bigquery.SchemaField("payout_block_time", "TIMESTAMP"),
            bigquery.SchemaField("runtime", "INT64"),
            bigquery.SchemaField("row_id", "INT64"),
            bigquery.SchemaField("row_time", "TIMESTAMP"),
        ],
        # 'query_select': 'SELECT * FROM blocks',
        'write_disposition': WRITE_DISPOSITION,
        'id_col_name': 'row_id',
        'update_type': UPDATE_TYPE,
        'file_size_limit_rows': 5_000_000,
    },

    'extrinsics': {
        'schema': [
            bigquery.SchemaField("network_id", "INT64"),
            bigquery.SchemaField("extrinsic_id", "STRING"),
            bigquery.SchemaField("block_id", "INT64"),
            bigquery.SchemaField("success", "BOOLEAN"),
            bigquery.SchemaField("parent_id", "STRING"),
            bigquery.SchemaField("section", "STRING"),
            bigquery.SchemaField("method", "STRING"),
            bigquery.SchemaField("mortal_period", "INT64"),
            bigquery.SchemaField("mortal_phase", "INT64"),
            bigquery.SchemaField("is_signed", "BOOLEAN"),
            bigquery.SchemaField("signer", "STRING"),
            bigquery.SchemaField("tip", "NUMERIC"),
            bigquery.SchemaField("nonce", "FLOAT64"),
            bigquery.SchemaField("ref_event_ids", "STRING"),
            bigquery.SchemaField("version", "INT64"),
            bigquery.SchemaField("extrinsic", "STRING"),
            bigquery.SchemaField("row_id", "INT64"),
            bigquery.SchemaField("row_time", "TIMESTAMP"),
        ],
        # 'query_select': 'SELECT * FROM extrinsics',
        'write_disposition': WRITE_DISPOSITION,
        'id_col_name': 'row_id',
        'update_type': UPDATE_TYPE,
        'file_size_limit_rows': 5_000_000,
    },

    'events': {
        'schema': [
            bigquery.SchemaField("network_id", "INT64"),
            bigquery.SchemaField("event_id", "STRING"),
            bigquery.SchemaField("block_id", "INT64"),
            bigquery.SchemaField("section", "STRING"),
            bigquery.SchemaField("method", "STRING"),
            bigquery.SchemaField("event", "STRING"),
            bigquery.SchemaField("row_id", "INT64"),
            bigquery.SchemaField("row_time", "TIMESTAMP"),
        ],
        # 'query_select': 'SELECT * FROM events',
        'write_disposition': WRITE_DISPOSITION,
        'id_col_name': 'row_id',
        'update_type': UPDATE_TYPE,
        'file_size_limit_rows': 20_000_000,
    },

    'collators': {
        'schema': [
            bigquery.SchemaField("network_id", "INT64"),
            bigquery.SchemaField("round_id", "INT64"),
            bigquery.SchemaField("account_id", "STRING"),
            bigquery.SchemaField("total_stake", "NUMERIC"),
            bigquery.SchemaField("own_stake", "NUMERIC"),
            bigquery.SchemaField("delegators_count", "INT64"),
            bigquery.SchemaField("total_reward_points", "INT64"),
            bigquery.SchemaField("total_reward", "NUMERIC"),
            bigquery.SchemaField("payout_block_id", "INT64"),
            bigquery.SchemaField("payout_block_time", "TIMESTAMP"),
            bigquery.SchemaField("row_id", "INT64"),
            bigquery.SchemaField("collator_reward", "NUMERIC"),
            bigquery.SchemaField("active", "BOOLEAN"),
            bigquery.SchemaField("row_time", "TIMESTAMP"),
        ],
        # 'query_select': 'SELECT * FROM validators',
        'write_disposition': WRITE_DISPOSITION,
        'id_col_name': 'row_id',
        'update_type': UPDATE_TYPE,
        'file_size_limit_rows': 5_000_000,
    },

    'stake_collators': {
        'schema': [
            bigquery.SchemaField("network_id", "INT64"),
            bigquery.SchemaField("round_id", "INT64"),
            bigquery.SchemaField("account_id", "STRING"),
            bigquery.SchemaField("active", "BOOLEAN"),
            bigquery.SchemaField("total_stake", "NUMERIC"),
            bigquery.SchemaField("own_stake", "NUMERIC"),
            bigquery.SchemaField("delegators_count", "INT64"),
            bigquery.SchemaField("row_id", "INT64"),
            bigquery.SchemaField("row_time", "TIMESTAMP"),
        ],
        # 'query_select': 'SELECT * FROM validators',
        'write_disposition': WRITE_DISPOSITION,
        'id_col_name': 'row_id',
        'update_type': UPDATE_TYPE,
        'file_size_limit_rows': 5_000_000,
    },

    'rewards_collators': {
        'schema': [
            bigquery.SchemaField("network_id", "INT64"),
            bigquery.SchemaField("round_id", "INT64"),
            bigquery.SchemaField("account_id", "STRING"),
            bigquery.SchemaField("active", "BOOLEAN"),
            bigquery.SchemaField("final_stake", "NUMERIC"),
            bigquery.SchemaField("total_reward_points", "INT64"),
            bigquery.SchemaField("total_reward", "NUMERIC"),
            bigquery.SchemaField("collator_reward", "NUMERIC"),
            bigquery.SchemaField("payout_block_id", "INT64"),
            bigquery.SchemaField("payout_block_time", "TIMESTAMP"),
            bigquery.SchemaField("row_id", "INT64"),
            bigquery.SchemaField("row_time", "TIMESTAMP"),
        ],
        # 'query_select': 'SELECT * FROM validators',
        'write_disposition': WRITE_DISPOSITION,
        'id_col_name': 'row_id',
        'update_type': UPDATE_TYPE,
        'file_size_limit_rows': 5_000_000,
    },

    'delegators': {
        'schema': [
            bigquery.SchemaField("network_id", "INT64"),
            bigquery.SchemaField("round_id", "INT64"),
            bigquery.SchemaField("account_id", "STRING"),
            bigquery.SchemaField("collator_id", "STRING"),
            bigquery.SchemaField("amount", "NUMERIC"),
            bigquery.SchemaField("reward", "NUMERIC"),
            bigquery.SchemaField("payout_block_id", "INT64"),
            bigquery.SchemaField("payout_block_time", "TIMESTAMP"),
            bigquery.SchemaField("row_id", "INT64"),
            bigquery.SchemaField("final_amount", "NUMERIC"),
            bigquery.SchemaField("row_time", "TIMESTAMP"),
        ],
        # 'query_select': 'SELECT * FROM nominators',
        'write_disposition': WRITE_DISPOSITION,
        'id_col_name': 'row_id',
        'update_type': UPDATE_TYPE,
        'file_size_limit_rows': 5_000_000,
    },

    'stake_delegators': {
        'schema': [
            bigquery.SchemaField("network_id", "INT64"),
            bigquery.SchemaField("round_id", "INT64"),
            bigquery.SchemaField("account_id", "STRING"),
            bigquery.SchemaField("collator_id", "STRING"),
            bigquery.SchemaField("amount", "NUMERIC"),
            bigquery.SchemaField("row_id", "INT64"),
            bigquery.SchemaField("row_time", "TIMESTAMP"),
        ],
        # 'query_select': 'SELECT * FROM nominators',
        'write_disposition': WRITE_DISPOSITION,
        'id_col_name': 'row_id',
        'update_type': UPDATE_TYPE,
        'file_size_limit_rows': 5_000_000,
    },

    'rewards_delegators': {
        'schema': [
            bigquery.SchemaField("network_id", "INT64"),
            bigquery.SchemaField("round_id", "INT64"),
            bigquery.SchemaField("account_id", "STRING"),
            bigquery.SchemaField("collator_id", "STRING"),
            bigquery.SchemaField("final_amount", "NUMERIC"),
            bigquery.SchemaField("reward", "NUMERIC"),
            bigquery.SchemaField("payout_block_id", "INT64"),
            bigquery.SchemaField("payout_block_time", "TIMESTAMP"),
            bigquery.SchemaField("row_id", "INT64"),
            bigquery.SchemaField("row_time", "TIMESTAMP"),
        ],
        # 'query_select': 'SELECT * FROM nominators',
        'write_disposition': WRITE_DISPOSITION,
        'id_col_name': 'row_id',
        'update_type': UPDATE_TYPE,
        'file_size_limit_rows': 5_000_000,
    },

    'networks': {
        'schema': [
            bigquery.SchemaField("network_id", "INT64"),
            bigquery.SchemaField("name", "STRING"),
            bigquery.SchemaField("decimals", "INT64"),
        ],
        'write_disposition': WRITE_DISPOSITION,
        'id_col_name': 'network_id',
        'update_type': UPDATE_TYPE,
        'file_size_limit_rows': 5_000_000,
        # 'query_select': 'SELECT network_id, name, decimals FROM networks',
        # 'write_disposition': 'truncate'
    },

    'total_issuance': {
        'schema': [
            bigquery.SchemaField("network_id", "INT64"),
            bigquery.SchemaField("block_id", "INT64"),
            bigquery.SchemaField("total_issuance", "FLOAT64"),
            bigquery.SchemaField("row_id", "INT64"),
            bigquery.SchemaField("row_time", "TIMESTAMP"),
        ],
        'write_disposition': WRITE_DISPOSITION,
        'id_col_name': 'row_id',
        'update_type': UPDATE_TYPE,
        'file_size_limit_rows': 5_000_000,
        # 'query_select': 'SELECT network_id, block_id, total_issuance, row_id, row_time FROM total_issuance',
        # 'write_disposition': 'truncate'
    },

    'accounts': {
        'schema': [
            bigquery.SchemaField("network_id", "INT64"),
            bigquery.SchemaField("account_id", "STRING"),
            bigquery.SchemaField("created_at_block_id", "INT64"),
            bigquery.SchemaField("killed_at_block_id", "INT64"),
            bigquery.SchemaField("judgement_status", "STRING"),
            bigquery.SchemaField("registrar_index", "INT64"),
            bigquery.SchemaField("row_id", "INT64"),
            bigquery.SchemaField("row_time", "TIMESTAMP"),
        ],
        # 'query_select': 'SELECT * FROM networks',
        'write_disposition': WRITE_DISPOSITION,
        'id_col_name': 'row_id',
        'update_type': UPDATE_TYPE,
        'file_size_limit_rows': 5_000_000,
    },

    'identities': {
        'schema': [
            bigquery.SchemaField("network_id", "INT64"),
            bigquery.SchemaField("account_id", "STRING"),
            bigquery.SchemaField("parent_account_id", "STRING"),
            bigquery.SchemaField("display", "STRING"),
            bigquery.SchemaField("legal", "STRING"),
            bigquery.SchemaField("web", "STRING"),
            bigquery.SchemaField("riot", "STRING"),
            bigquery.SchemaField("email", "STRING"),
            bigquery.SchemaField("twitter", "STRING"),
            bigquery.SchemaField("updated_at_block_id", "INT64"),
            bigquery.SchemaField("row_id", "INT64"),
            bigquery.SchemaField("row_time", "TIMESTAMP"),
        ],
        # 'query_select': 'SELECT * FROM networks',
        'write_disposition': 'truncate',#WRITE_DISPOSITION,
        'id_col_name': 'row_id',
        'update_type': 'full', #UPDATE_TYPE,
        'file_size_limit_rows': 5_000_000,
        # 'query_select': 'SELECT network_id, account_id, parent_account_id, display, legal, web, riot, email, twitter,
        #                  updated_at_block_id, row_id, row_time FROM total_issuance',
        # 'write_disposition': 'truncate'
    },
    'sli_metrics': {
        'schema': [
            bigquery.SchemaField("network_id", "INT64"),
            bigquery.SchemaField("entity", "STRING"),
            bigquery.SchemaField("entity_id", "INT64"),
            bigquery.SchemaField("name", "STRING"),
            bigquery.SchemaField("value", "INT64"),
            bigquery.SchemaField("row_id", "INT64"),
            bigquery.SchemaField("row_time", "TIMESTAMP"),
        ],
        'write_disposition': WRITE_DISPOSITION,
        'id_col_name': 'row_id',
        'update_type': UPDATE_TYPE,
        'file_size_limit_rows': 5_000_000,
    },
    'balances': {
        'schema': [
            bigquery.SchemaField("network_id", "INT64"),
            bigquery.SchemaField("block_id", "INT64"),
            bigquery.SchemaField("account_id", "STRING"),
            bigquery.SchemaField("blake2_hash", "STRING"),
            bigquery.SchemaField("nonce", "INT64"),
            bigquery.SchemaField("consumers", "INT64"),
            bigquery.SchemaField("providers", "INT64"),
            bigquery.SchemaField("sufficients", "INT64"),
            bigquery.SchemaField("free", "FLOAT64"),
            bigquery.SchemaField("reserved", "FLOAT64"),
            bigquery.SchemaField("miscFrozen", "FLOAT64"),
            bigquery.SchemaField("feeFrozen", "FLOAT64"),
            bigquery.SchemaField("row_id", "INT64"),
            bigquery.SchemaField("row_time", "TIMESTAMP"),
        ],
        'write_disposition': WRITE_DISPOSITION,
        'id_col_name': 'row_id',
        'update_type': UPDATE_TYPE,
        'file_size_limit_rows': 5_000_000,
    }
}
