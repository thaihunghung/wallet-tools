from eth_account import Account
from loguru import logger
import os

# Bật tính năng HD Wallet chưa được kiểm duyệt trong eth_account (chấp nhận rủi ro bảo mật nếu dùng production)
Account.enable_unaudited_hdwallet_features()

# Ghi log bắt đầu quá trình tạo ví
logger.info('Generating new private keys, addresses, and mnemonic phrases...')

# Số lượng ví cần tạo
NUM_WALLETS = 100

# Tên file xuất dữ liệu
private_keys_file = 'private_keys100.txt'   # File chứa private key
address_file = 'address100.txt'             # File chứa địa chỉ ví
mnemonic_file = 'mnemonic_phrases100.txt'   # File chứa mnemonic phrase

# Xóa các file cũ nếu đã tồn tại để tránh ghi đè không kiểm soát
if os.path.exists(private_keys_file):
    os.remove(private_keys_file)
if os.path.exists(address_file):
    os.remove(address_file)
if os.path.exists(mnemonic_file):
    os.remove(mnemonic_file)

# Mở các file để ghi dữ liệu private key, address và mnemonic
with open(private_keys_file, 'w', encoding='utf-8') as pk_file, \
     open(address_file, 'w', encoding='utf-8') as addr_file, \
     open(mnemonic_file, 'w', encoding='utf-8') as mnemo_file:

    # Tạo vòng lặp để tạo ví theo số lượng yêu cầu
    for _ in range(NUM_WALLETS):
        # Tạo account mới kèm mnemonic phrase
        account, mnemonic = Account.create_with_mnemonic()

        private_key = account.key.hex()  # Lấy private key dưới dạng hex
        address = account.address        # Lấy địa chỉ ví

        # Ghi thông tin vào các file tương ứng
        pk_file.write(f'{private_key}\n')
        addr_file.write(f'{address}\n')
        mnemo_file.write(f'{mnemonic}\n')

        # Log thông tin ví được tạo
        logger.info(f'Generated address: {address} with mnemonic phrase: {mnemonic}')

# Thông báo hoàn tất quá trình tạo ví
logger.success('Successfully created new wallets, mnemonic phrases and saved them to files.')
