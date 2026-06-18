
def calculate_discount(price, user_type, is_member):
    """
    业务逻辑：VIP会员8折，普通会员9折，非会员原价
    """
    # ⚠️ BUG：非会员但 user_type="vip" 也会打8折
    if user_type == "vip":
        return price * 0.8
    elif is_member:
        return price * 0.9
    else:
        return price

