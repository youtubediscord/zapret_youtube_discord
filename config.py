BIN_FOLDER = "bin"
LISTS_FOLDER = "lists"
APP_VERSION = "11.4.0"

# Базовые команды и пути
WF_TCP = "--wf-tcp=80,443"
WF_UDP = "--wf-udp=443,50000-50100"

# Пути к файлам через переменные для централизованного управления
YT = f"--filter-tcp=443 --hostlist={LISTS_FOLDER}/youtube.txt"
YT_2 = f"--filter-tcp=443 --hostlist={LISTS_FOLDER}/youtube_v2.txt"
YGV = f"--filter-tcp=443 --hostlist={LISTS_FOLDER}/youtubeGV.txt"
YQ = f"--filter-udp=443 --hostlist={LISTS_FOLDER}/youtubeQ.txt"
DISTCP = f"--filter-tcp=443 --hostlist={LISTS_FOLDER}/discord.txt"
DISTCP80 = "--filter-tcp=80"
DISUDP = f"--filter-udp=443 --hostlist={LISTS_FOLDER}/discord.txt"
OTHER = f"--filter-tcp=443 --hostlist={LISTS_FOLDER}/other.txt"
faceinsta = f"--filter-tcp=443 --hostlist={LISTS_FOLDER}/faceinsta.txt --dpi-desync=split2 --dpi-desync-split-seqovl=652 --dpi-desync-split-pos=2 --dpi-desync-split-seqovl-pattern={BIN_FOLDER}/tls_clienthello_4.bin --new"
TCP80 = "--filter-tcp=80 --dpi-desync=fake,fakedsplit --dpi-desync-autottl=2 --dpi-desync-fooling=md5sig --new"
# добавить все из архива гитхаба flow

# YouTube конфигурации
YT1 = f"{YT} --dpi-desync=fake,split2 --dpi-desync-split-seqovl=2 --dpi-desync-split-pos=3 --dpi-desync-fake-tls={BIN_FOLDER}/tls_clienthello_www_google_com.bin --dpi-desync-ttl=3 --new"
YT2 = f"{YT} --dpi-desync=fake,split2 --dpi-desync-split-seqovl=2 --dpi-desync-split-pos=3 --new"
YT3 = f"{YT} --dpi-desync=split --dpi-desync-split-seqovl=1 --dpi-desync-split-tls=sniext --dpi-desync-fake-tls={BIN_FOLDER}/tls_clienthello_www_google_com.bin --dpi-desync-ttl=1 --new"
YT4 = f"{YT} --dpi-desync=split --dpi-desync-split-pos=1 --dpi-desync-fooling=badseq --dpi-desync-repeats=10 --dpi-desync-autottl=2 --new"
YT5 = f"{YT} --dpi-desync=fake,split2 --dpi-desync-split-seqovl=2 --dpi-desync-split-pos=3 --dpi-desync-fake-tls={BIN_FOLDER}/tls_clienthello_2.bin --dpi-desync-autottl=2 --new"
YT6 = f"{YT} --dpi-desync=fake,split2 --dpi-desync-split-seqovl=1 --dpi-desync-split-tls=sniext --dpi-desync-fake-tls={BIN_FOLDER}/tls_clienthello_www_google_com.bin --dpi-desync-ttl=4 --new"
YT7 = f"{YT} --dpi-desync=split --dpi-desync-split-pos=3 --dpi-desync-repeats=4 --dpi-desync-autottl=1 --new"
YT8 = f"{YT} --dpi-desync=split --dpi-desync-split-pos=1 --dpi-desync-fooling=badseq --dpi-desync-repeats=10 --dpi-desync-cutoff=d2 --dpi-desync-ttl=3 --new"
YT9 = f"{YT} --dpi-desync=fake,multisplit --dpi-desync-split-seqovl=2 --dpi-desync-split-pos=3 --dpi-desync-fake-tls={BIN_FOLDER}/tls_clienthello_2.bin --dpi-desync-ttl=3 --new"
YT10 = f"{YT_2} --dpi-desync=multisplit --dpi-desync-split-seqovl=1 --dpi-desync-split-pos=midsld+1 --new"
YT11 = f"{YT} --dpi-desync=fake,multidisorder --dpi-desync-split-pos=1,midsld --dpi-desync-repeats=11 --dpi-desync-fooling=md5sig --dpi-desync-fake-tls={BIN_FOLDER}/tls_clienthello_www_google_com.bin --new"
#YoutubeFix (ALT v10).bat
Ankddev10_4 = f"{YT} --dpi-desync=syndata,multidisorder2 --dpi-desync-split-pos=4 --dpi-desync-repeats=10 --dpi-desync-fooling=md5sig --dpi-desync-fake-tls={BIN_FOLDER}/tls_clienthello_vk_com_kyber.bin --new"

# GeoVideo конфигурации
YGV1 = f"{YGV} --dpi-desync=split --dpi-desync-split-pos=1 --dpi-desync-fooling=badseq --dpi-desync-repeats=10 --dpi-desync-cutoff=d2 --dpi-desync-ttl=4 --new"
YGV2 = f"{YGV} --dpi-desync=fakedsplit --dpi-desync-split-pos=1 --dpi-desync-fooling=badseq --dpi-desync-repeats=10 --dpi-desync-ttl=4 --new"
YGV3 = f"{YGV} --dpi-desync=multisplit --dpi-desync-split-seqovl=1 --dpi-desync-split-pos=midsld-1 --new"

# YRTMP конфигурации
YRTMP1 = f"--filter-tcp=443 --ipset={LISTS_FOLDER}/russia-youtube-rtmps.txt --dpi-desync=syndata --dpi-desync-fake-syndata={BIN_FOLDER}/tls_clienthello_4.bin --dpi-desync-autottl --new"
YRTMP2 = "--filter-tcp=443 --ipset-ip=XXX.XXX.XXX.XXX/XX,XXX.XXX.XXX.XXX/XX --wssize=1:6 --hostlist-domains=googlevideo.com --dpi-desync=multidisorder --dpi-desync-split-seqovl=1 --dpi-desync-split-pos=1,host+2,sld+2,sld+5,sniext+1,sniext+2,endhost-2 --new"

# Discord TCP конфигурации
DISTCP1 = f"{DISTCP} --dpi-desync=split --dpi-desync-split-pos=1 --dpi-desync-fooling=badseq --dpi-desync-repeats=10 --dpi-desync-ttl=4 --new"
DISTCP2 = f"{DISTCP} --dpi-desync=split2 --dpi-desync-split-seqovl=652 --dpi-desync-split-pos=2 --dpi-desync-split-seqovl-pattern={BIN_FOLDER}/tls_clienthello_4.bin --new"
DISTCP3 = f"{DISTCP} --dpi-desync=fake,split --dpi-desync-repeats=6 --dpi-desync-fooling=badseq --dpi-desync-fake-tls={BIN_FOLDER}/tls_clienthello_www_google_com.bin --new"
DISTCP4 = f"{DISTCP} --dpi-desync=fake,split2 --dpi-desync-ttl=1 --dpi-desync-autottl=5 --dpi-desync-repeats=6 --dpi-desync-fake-tls={BIN_FOLDER}/tls_clienthello_sberbank_ru.bin --new"
DISTCP5 = f"{DISTCP} --dpi-desync=syndata --dpi-desync-fake-syndata={BIN_FOLDER}/tls_clienthello_3.bin --dpi-desync-ttl=5 --new"
DISTCP6 = f"{DISTCP} --dpi-desync=fake,split --dpi-desync-autottl=2 --dpi-desync-repeats=6 --dpi-desync-fooling=badseq --dpi-desync-fake-tls={BIN_FOLDER}/tls_clienthello_www_google_com.bin --new"
DISTCP7 = f"{DISTCP} --dpi-desync=fake,split2 --dpi-desync-split-seqovl=1 --dpi-desync-split-tls=sniext --dpi-desync-fake-tls={BIN_FOLDER}/tls_clienthello_4.bin --dpi-desync-ttl=4 --new"
DISTCP8 = f"{DISTCP} --dpi-desync=fake,split2 --dpi-desync-split-seqovl=1 --dpi-desync-split-tls=sniext --dpi-desync-fake-tls={BIN_FOLDER}/tls_clienthello_www_google_com.bin --dpi-desync-ttl=2 --new"
DISTCP9 = f"{DISTCP} --dpi-desync=split --dpi-desync-split-pos=1 --dpi-desync-fooling=badseq --dpi-desync-repeats=10 --dpi-desync-autottl --new"
DISTCP10 = f"{DISTCP} --dpi-desync=split --dpi-desync-split-pos=1 --dpi-desync-fooling=badseq --dpi-desync-repeats=10 --dpi-desync-ttl=3 --new"
DISTCP11 = f"{DISTCP} --dpi-desync=fakedsplit --dpi-desync-split-pos=1 --dpi-desync-fooling=badseq --dpi-desync-repeats=10 --dpi-desync-autottl --new"
DISTCP12 = f"{DISTCP} --dpi-desync=multisplit --dpi-desync-split-seqovl=1 --dpi-desync-split-pos=midsld+1 --new"
DISTCP13 = f"{DISTCP80} {DISTCP} --dpi-desync=fake,multidisorder --dpi-desync-split-pos=midsld --dpi-desync-repeats=6 --dpi-desync-fooling=badseq,md5sig --new"
DISTCP80_CONFIG = f"--filter-tcp=80 --hostlist={LISTS_FOLDER}/discord.txt --dpi-desync=fake,split2 --dpi-desync-autottl=2 --dpi-desync-fooling=md5sig --new"
#DiscordFix (ALT v10).bat
Ankddev10_1 = f"{DISTCP} --dpi-desync=syndata,disorder2 --dpi-desync-split-pos=3 --dpi-desync-repeats=11 --dpi-desync-fooling=badseq --dpi-desync-fake-tls={BIN_FOLDER}/tls_clienthello_www_google_com.bin --new"

UDP1 = f"--filter-udp=50000-59000 --dpi-desync=fake,split2 --dpi-desync-any-protocol --dpi-desync-cutoff=d2 --dpi-desync-fake-quic={BIN_FOLDER}/quic_test_00.bin --new"
#$UDP6 = "--filter-udp=50000-65535 --dpi-desync=fake,split2 --dpi-desync-any-protocol --dpi-desync-cutoff=d2 --dpi-desync-fake-quic={BIN_FOLDER}/quic_test_00.bin --new"
UDP2 = f"--filter-udp=50000-59000 --dpi-desync=fake --dpi-desync-any-protocol --dpi-desync-cutoff=d3 --dpi-desync-repeats=6 --new"
UDP3 = f"--filter-udp=50000-59000 --dpi-desync=fake --dpi-desync-any-protocol --dpi-desync-cutoff=d3 --dpi-desync-repeats=6 --dpi-desync-fake-quic={BIN_FOLDER}/quic_initial_www_google_com.bin --new"
UDP4 = f"--filter-udp=50000-59000 --dpi-desync=fake,tamper --dpi-desync-any-protocol --dpi-desync-cutoff=d3 --dpi-desync-repeats=6 --dpi-desync-fake-quic={BIN_FOLDER}/quic_initial_www_google_com.bin --new"
UDP5 = f"--filter-udp=50000-59000 --dpi-desync=fake,tamper --dpi-desync-any-protocol --dpi-desync-cutoff=n5 --dpi-desync-repeats=10 --dpi-desync-fake-quic={BIN_FOLDER}/quic_initial_www_google_com.bin --new"
UDP7 = f"--filter-udp=50000-50090 --dpi-desync=fake --dpi-desync-any-protocol --dpi-desync-cutoff=n3 --new"
UDP8 = f"--filter-udp=443 --dpi-desync=fake --dpi-desync-repeats=11 --new"

# YouTube QUIC конфигурации
YQ1 = f"--dpi-desync=fake --dpi-desync-repeats=2 --dpi-desync-cutoff=n2 --dpi-desync-fake-quic={BIN_FOLDER}/quic_test_00.bin --new"
YQ2 = f"{YQ} --dpi-desync=fake --dpi-desync-repeats=4 --dpi-desync-fake-quic={BIN_FOLDER}/quic_initial_www_google_com.bin --new"
YQ3 = f"{YQ} --dpi-desync=fake --dpi-desync-repeats=4 --dpi-desync-fake-quic={BIN_FOLDER}/quic_1.bin --new"
YQ4 = f"{YQ} --dpi-desync=fake --dpi-desync-repeats=11 --dpi-desync-fake-quic={BIN_FOLDER}/quic_initial_www_google_com.bin --new"
YQ5 = f"{YQ} --dpi-desync=fake --dpi-desync-repeats=2 --dpi-desync-cutoff=n2 --dpi-desync-fake-quic={BIN_FOLDER}/quic_initial_www_google_com.bin --new"
YQ6 = f"{YQ} --dpi-desync=fake --dpi-desync-fake-quic={BIN_FOLDER}/quic_1.bin --dpi-desync-repeats=4 --new"
YQ7 = f"{YQ} --dpi-desync=fake,udplen --dpi-desync-udplen-increment=2 --dpi-desync-fake-quic={BIN_FOLDER}/quic_3.bin --dpi-desync-cutoff=n3 --dpi-desync-repeats=2 --new"
YQ8 = f"{YQ} --dpi-desync=fake,udplen --dpi-desync-udplen-increment=4 --dpi-desync-fake-quic={BIN_FOLDER}/quic_3.bin --dpi-desync-cutoff=n3 --dpi-desync-repeats=2 --new"
YQ9 = f"{YQ} --dpi-desync=fake --dpi-desync-repeats=11 --dpi-desync-fake-quic={BIN_FOLDER}/quic_initial_www_google_com.bin --new"
Ankddev10_5 = f"{YQ} --dpi-desync=fake,split2 --dpi-desync-repeats=10 --dpi-desync-udplen-increment=25 --dpi-desync-fake-quic={BIN_FOLDER}/quic_initial_www_google_com.bin --new"

# Discord UDP конфигурации
DISUDP1 = f"{DISUDP} --dpi-desync=fake --dpi-desync-udplen-increment=10 --dpi-desync-repeats=7 --dpi-desync-udplen-pattern=0xDEADBEEF --dpi-desync-fake-quic={BIN_FOLDER}/quic_test_00.bin --dpi-desync-cutoff=n2 --new"
DISUDP2 = f"{DISUDP} --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic={BIN_FOLDER}/quic_1.bin --new"
DISUDP3 = f"{DISUDP} --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic={BIN_FOLDER}/quic_initial_www_google_com.bin --new"
DISUDP4 = f"{DISUDP} --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic={BIN_FOLDER}/quic_initial_vk_com.bin --new"
DISUDP5 = f"{DISUDP} --dpi-desync=fake --dpi-desync-udplen-increment=10 --dpi-desync-repeats=7 --dpi-desync-udplen-pattern=0xDEADBEEF --dpi-desync-fake-quic={BIN_FOLDER}\quic_initial_www_google_com.bin --new"
DISUDP6 = f"{DISUDP} --dpi-desync=fake,split2 --dpi-desync-udplen-increment=10 --dpi-desync-repeats=6 --dpi-desync-udplen-pattern=0xDEADBEEF --dpi-desync-fake-quic={BIN_FOLDER}\quic_initial_www_google_com.bin --new"
DISUDP7 = f"{DISUDP} --dpi-desync=fake --dpi-desync-udplen-increment=10 --dpi-desync-repeats=6 --dpi-desync-udplen-pattern=0xDEADBEEF --dpi-desync-fake-quic={BIN_FOLDER}\quic_initial_www_google_com.bin --new"
DISUDP8 = f"{DISUDP} --dpi-desync=fake --dpi-desync-udplen-increment=10 --dpi-desync-udplen-pattern=0xDEADBEEF --dpi-desync-fake-quic={BIN_FOLDER}\quic_2.bin --dpi-desync-repeats=8 --dpi-desync-cutoff=n2 --new"
DISUDP9 = f"{DISUDP} --dpi-desync=fake,udplen --dpi-desync-udplen-increment=5 --dpi-desync-udplen-pattern=0xDEADBEEF --dpi-desync-fake-quic={BIN_FOLDER}\quic_2.bin --dpi-desync-repeats=7 --dpi-desync-cutoff=n2 --new"
Ankddev10_2 = f"{DISUDP} --dpi-desync=fake,split2 --dpi-desync-repeats=11 --dpi-desync-udplen-increment=15 --dpi-desync-fake-quic={BIN_FOLDER}\quic_initial_www_google_com.bin --new"

DISIP1 = f"--filter-udp=50000-50010 --ipset={LISTS_FOLDER}/ipset-discord.txt --dpi-desync=fake --dpi-desync-any-protocol --dpi-desync-cutoff=d3 --dpi-desync-repeats=6 --new"
DISIP2 = f"--filter-udp=50000-65535 --ipset={LISTS_FOLDER}/ipset-discord.txt --dpi-desync=fake --dpi-desync-any-protocol --dpi-desync-cutoff=d3 --dpi-desync-repeats=6 --new"
DISIP3 = f"--filter-udp=50000-59000 --dpi-desync=fake --dpi-desync-any-protocol --dpi-desync-cutoff=n2 --dpi-desync-fake-quic={BIN_FOLDER}/quic_initial_www_google_com.bin --new"
DISIP4 = f"--filter-udp=50000-50099 --dpi-desync=fake --dpi-desync-any-protocol --dpi-desync-cutoff=d2 --dpi-desync-fake-quic={BIN_FOLDER}/quic_1.bin --new"
DISIP5 = f"--filter-tcp=443 --ipset={LISTS_FOLDER}/ipset-discord.txt --dpi-desync=syndata --dpi-desync-fake-syndata={BIN_FOLDER}/tls_clienthello_3.bin --dpi-desync-autottl --new"
DISIP6 = f"--filter-udp=50000-50099 --ipset={LISTS_FOLDER}/ipset-discord.txt --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-any-protocol --dpi-desync-cutoff=n4 --new"
Ankddev10_3 = f"--filter-udp=50000-50099 --ipset={LISTS_FOLDER}/ipset-discord.txt --dpi-desync=fake,tamper --dpi-desync-any-protocol --dpi-desync-cutoff=d5 --dpi-desync-repeats=11 --new"

other = f"--filter-tcp=443 --hostlist={LISTS_FOLDER}/other.txt"
other1 = f"{other} --dpi-desync=fake,split2 --dpi-desync-split-seqovl=1 --dpi-desync-split-tls=sniext --dpi-desync-fake-tls={BIN_FOLDER}/tls_clienthello_3.bin --dpi-desync-ttl=2 --new"
other2 = f"{other} --dpi-desync=fake,multisplit --dpi-desync-fooling=md5sig --dpi-desync-autottl --new"
other3 = f"{other} --dpi-desync=fake,multisplit --dpi-desync-split-seqovl=1 --dpi-desync-split-pos=1 --dpi-desync-fake-tls={BIN_FOLDER}/tls_clienthello_vk_com.bin --dpi-desync-ttl=5 --new"
other4 = f"{other} --dpi-desync=fake,multisplit --dpi-desync-split-seqovl=1 --dpi-desync-split-pos=midsld-1 --dpi-desync-fooling=md5sig,badseq --dpi-desync-fake-tls={BIN_FOLDER}/tls_clienthello_4.bin --dpi-desync-ttl=2 --new"
other5 = f"{other} --dpi-desync=fake,multidisorder --dpi-desync-split-pos=midsld --dpi-desync-repeats=6 --dpi-desync-fooling=badseq,md5sig --new"

DPI_COMMANDS = {
    "06.01.2025":  f"{WF_TCP} --wf-udp=443,50000-50100 {YRTMP1} {YQ8} {YT10} {YGV3} {other1} {DISIP5} {DISTCP11} {DISUDP9} {UDP7} {YRTMP2} {faceinsta}",
    "lite orig v1":  f"{WF_TCP} --wf-udp=443,50000-50100 {faceinsta} {TCP80} {YT11} {YQ9} {other3} {DISTCP13} {UDP8} {DISIP6}",
    "Discord TCP 80":  f"{WF_TCP} --wf-udp=443,50000-59000 {YQ1} {YGV1} {YT1} {DISTCP80} {DISUDP2} {UDP2} {DISTCP2} {other1} {faceinsta}",
    "Discord fake":  f"{WF_TCP} --wf-udp=443,50000-59000 {YQ1} {YGV1} {YT1} {DISUDP1} {UDP1} {DISTCP1} {other1} {faceinsta}",
    "Discord fake и split":  f"{WF_TCP} --wf-udp=443,50000-50100 {DISUDP3} {DISIP1} {DISTCP80} {DISTCP3} {YQ1} {YGV1} {YT2} {other1} {faceinsta}",
    "Ultimate Fix ALT Beeline-Rostelekom":  f"{WF_TCP} --wf-udp=443,50000-65535 {DISUDP4} {DISIP2} {DISTCP80} {DISTCP4} {YQ1} {YGV1} {YT2} {other1} {faceinsta}",
    "split с sniext":  f"{WF_TCP} --wf-udp=443,50000-59000 {YQ2} {YGV3} {YT3} {DISTCP5} {DISUDP5} {DISIP3} {other1} {faceinsta}",
    "split с badseq":  f"{WF_TCP} --wf-udp=443,50000-59000 {YQ2} {YGV1} {YT4} {DISTCP5} {DISUDP5} {DISIP3} {other1} {faceinsta}",
    "Rostelecom & Megafon":  f"{WF_TCP} --wf-udp=443,50000-59000 {YQ2} {YT4} {DISUDP3} {UDP3} {DISTCP6} {other1} {faceinsta}",
    "Rostelecom v2":  f"{WF_TCP} --wf-udp=443,50000-59000 {YQ3} {YT5} {DISUDP3} {UDP3} {DISTCP6} {other1} {faceinsta}",
    "Other v1": f"--wf-l3=ipv4,ipv6 --wf-tcp=443 --wf-udp=443,50000-65535 {YQ4} {YT3} {DISTCP7} {DISUDP6} {UDP4} {other1} {faceinsta}",
    "Other v2": f"--wf-l3=ipv4,ipv6 --wf-tcp=443 --wf-udp=443,50000-65535 {YQ4} {YT6} {DISUDP7} {UDP5} {DISTCP8} {other1} {faceinsta}",
    "Ankddev v10": f"--wf-l3=ipv4,ipv6 --wf-tcp=443 --wf-udp=443,50000-65535 {Ankddev10_1} {Ankddev10_2} {Ankddev10_3} {Ankddev10_4} {Ankddev10_5}",
    "MGTS v1":  f"{WF_TCP} --wf-udp=443,50000-50010 {YGV1} {YT7} {DISIP1} {DISTCP9} {other1} {faceinsta}",
    "MGTS v2":  f"{WF_TCP} --wf-udp=443,50000-50900 {YT8} {DISTCP10} {YQ5} {DISUDP1} {other1} {faceinsta}",
    "MGTS v3":  f"{WF_TCP} --wf-udp=443,50000-50900 {YT7} {DISTCP10} {YQ5} {DISUDP1} {UDP1} {other1} {faceinsta}",
    "MGTS v4":  f"{WF_TCP} --wf-udp=443,50000-50900 {YQ1} {YGV3} {YT1} {DISUDP1} {UDP1} {DISTCP1} {other1} {faceinsta}",
    "Ultimate Config ZL":  f"{WF_TCP} --wf-udp=443,50000-50099 {YQ6} {YGV2} {YT9} {DISTCP11} {DISUDP8} {DISIP4} {other3} {faceinsta}",
    "Ultimate Config v2":  f"{WF_TCP} --wf-udp=443,50000-50090 {YRTMP1} {YQ7} {DISIP5} {DISTCP12} {DISUDP9} {UDP7} {YGV3} {other2} {other4} {faceinsta}"
}

DPI_COMMANDS2 = {
    "Стандартный Запуск": [
        "--wf-tcp=80,443", "--wf-udp=443,50000-50100",
        "--filter-tcp=80", "--hostlist=list-general.txt",
        "--dpi-desync=fake,split2", "--dpi-desync-autottl=2",
        "--dpi-desync-fooling=md5sig", "--new",
        "--filter-tcp=443", "--hostlist=list-general.txt",
        "--dpi-desync=fake,split", "--dpi-desync-autottl=2",
        "--dpi-desync-repeats=6", "--dpi-desync-fooling=badseq",
        "--dpi-desync-fake-tls=tls_clienthello_www_google_com.bin"
    ],
    "Alt Запуск 1": [
        "--wf-tcp=80,443", "--wf-udp=443,50000-50100",
        "--filter-udp=443", "--hostlist=list-general.txt",
        "--dpi-desync=fake", "--dpi-desync-repeats=6",
        "--dpi-desync-fake-quic=quic_initial_www_google_com.bin", "--new",
        "--filter-udp=50000-50100", "--ipset=ipset-discord.txt",
        "--dpi-desync=fake", "--dpi-desync-any-protocol",
        "--dpi-desync-cutoff=d3", "--dpi-desync-repeats=6", "--new",
        "--filter-tcp=80", "--hostlist=list-general.txt",
        "--dpi-desync=fake,split2", "--dpi-desync-autottl=2",
        "--dpi-desync-fooling=md5sig", "--new",
        "--filter-tcp=443", "--hostlist=list-general.txt",
        "--dpi-desync=fake,split", "--dpi-desync-autottl=5",
        "--dpi-desync-repeats=6", "--dpi-desync-fooling=badseq",
        "--dpi-desync-fake-tls=tls_clienthello_www_google_com.bin"
    ],
    "Alt Запуск 2": [
        "--wf-tcp=80,443", "--wf-udp=443,50000-50100",
        "--filter-udp=443", "--hostlist=list-general.txt",
        "--dpi-desync=fake", "--dpi-desync-repeats=6",
        "--dpi-desync-fake-quic=quic_initial_www_google_com.bin", "--new",
        "--filter-udp=50000-50100", "--ipset=ipset-discord.txt",
        "--dpi-desync=fake", "--dpi-desync-any-protocol",
        "--dpi-desync-cutoff=d3", "--dpi-desync-repeats=6", "--new",
        "--filter-tcp=80", "--hostlist=list-general.txt",
        "--dpi-desync=fake,split2", "--dpi-desync-autottl=2",
        "--dpi-desync-fooling=md5sig", "--new",
        "--filter-tcp=443", "--hostlist=list-general.txt",
        "--dpi-desync=split2", "--dpi-desync-split-seqovl=652",
        "--dpi-desync-split-pos=2",
        "--dpi-desync-split-seqovl-pattern=tls_clienthello_www_google_com.bin"
    ],
    "Alt Запуск 3": [
        "--wf-tcp=80,443", "--wf-udp=443,50000-50100",
        "--filter-udp=443", "--hostlist=list-general.txt",
        "--dpi-desync=fake", "--dpi-desync-repeats=6",
        "--dpi-desync-fake-quic=quic_initial_www_google_com.bin", "--new",
        "--filter-udp=50000-50100", "--ipset=ipset-discord.txt",
        "--dpi-desync=fake", "--dpi-desync-any-protocol",
        "--dpi-desync-cutoff=d3", "--dpi-desync-repeats=8", "--new",
        "--filter-tcp=80", "--hostlist=list-general.txt",
        "--dpi-desync=fake,split2", "--dpi-desync-autottl=2",
        "--dpi-desync-fooling=md5sig", "--new",
        "--filter-tcp=443", "--hostlist=list-general.txt",
        "--dpi-desync=fake,split2", "--dpi-desync-repeats=6",
        "--dpi-desync-fooling=md5sig",
        "--dpi-desync-fake-tls=tls_clienthello_www_google_com.bin"
    ],
    "Alt Запуск 4": [
        "--wf-tcp=80,443", "--wf-udp=443,50000-50100",
        "--filter-udp=443", "--hostlist=list-general.txt",
        "--dpi-desync=fake", "--dpi-desync-repeats=6",
        "--dpi-desync-fake-quic=quic_initial_www_google_com.bin", "--new",
        "--filter-udp=50000-50100", "--ipset=ipset-discord.txt",
        "--dpi-desync=fake", "--dpi-desync-any-protocol",
        "--dpi-desync-cutoff=d3", "--dpi-desync-repeats=6", "--new",
        "--filter-tcp=80", "--hostlist=list-general.txt",
        "--dpi-desync=fake,split2", "--dpi-desync-autottl=2",
        "--dpi-desync-fooling=md5sig", "--new",
        "--filter-l3=ipv4", "--filter-tcp=443", "--dpi-desync=syndata"
    ],
    "Alt Запуск 5": [
        "--wf-tcp=80,443", "--wf-udp=443,50000-50100",
        "--filter-udp=443", "--hostlist=list-general.txt",
        "--dpi-desync=fake", "--dpi-desync-repeats=6",
        "--dpi-desync-fake-quic=quic_initial_www_google_com.bin", "--new",
        "--filter-udp=50000-50100", "--ipset=ipset-discord.txt",
        "--dpi-desync=fake", "--dpi-desync-any-protocol",
        "--dpi-desync-cutoff=d3", "--dpi-desync-repeats=6", "--new",
        "--filter-tcp=80", "--hostlist=list-general.txt",
        "--dpi-desync=fake,split2", "--dpi-desync-autottl=2",
        "--dpi-desync-fooling=md5sig", "--new",
        "--filter-tcp=443", "--hostlist=list-general.txt",
        "--dpi-desync=fake,split", "--dpi-desync-autottl=2",
        "--dpi-desync-repeats=6", "--dpi-desync-fooling=badseq",
        "--dpi-desync-fake-tls=tls_clienthello_www_google_com.bin"
    ]
    # ... добавьте остальные конфигурации аналогично
}
