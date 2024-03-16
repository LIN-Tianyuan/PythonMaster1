def outer(logo):
    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")

    return inner


fn1 = outer("SCEFormation")
fn1("Hello")
fn1("World")

fn2 = outer("Phone")
fn2("Huawei")
fn2("Apple")
