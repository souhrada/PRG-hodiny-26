# datetime je příliš dlouhý název, proto jej importujeme pod zkratkou dt
import datetime as dt

# pod proměnnou cas uložíme současný čas
cas = dt.datetime.now()


print(cas)

print(cas.month)
print(cas.day)
print(cas.year)
print(cas.second)
print(cas.minute)


# deltatime se používá pro odečítání, přičítání nebo porovnání času
plus10 = cas + dt.timedelta(minutes=10)
print(f"za 10 minut od teď bude {plus10}")

cas_prestavky = dt.datetime(2026,10, 27, 15, 5)
print(cas_prestavky)

kolik_do_prestavky = cas_prestavky - cas
print(f"Do přestávky zbývá {kolik_do_prestavky}")


# vem čas, udělej z něj string, rozděl string tam, kde jsou dvojtečky, pak jej spoj s dvojtečkama, ale spoj pouze prvních 7 věcí
# str() vytvoří z něčeho string
# .split() rozděluje string na základě nějakého znaku (v našem případě dvojtečky)
# .join() spojuje do stringu a ke spojení používá znak (v našem případě dvojtečky)
# [:7] znamená od indexu 0 po 7
print(":".join(str(kolik_do_prestavky).split(":"))[:7])


