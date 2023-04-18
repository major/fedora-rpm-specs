%global intro %{expand:
This package exists only to obsolete other packages which need to be removed
from the distribution. Packages are listed here when they become uninstallable
and must be removed to allow upgrades to proceed cleanly, or when there is some
other strong reason to uninstall the package from user systems. The package
being retired (and potentially becoming unavailable in future releases of
Fedora) is not a reason to include it here, as long as it doesn't cause upgrade
problems.

Note that this package is not installable, but obsoletes other packages by being
available in the repository.}

# Provenpackagers are welcome to modify this package, but please don't
# obsolete packages unless there's a good reason, as described above.
# A bugzilla ticket or a link to package retirement commit should be
# always included.

# In particular, when a *subpackage* is removed, but not other
# subpackages built from the same source, it is usually better to add
# the Obsoletes to some other sibling subpackage built from the same
# source package.

# Please remember to add all of the necessary information. See below the
# Source0: line for a description of the format. It is important that
# everything be included; yanking packages from an end-user system is "serious
# business" and should not be done lightly or without making everything as
# clear as possible.

Name:       fedora-obsolete-packages
# Please keep the version equal to the targeted Fedora release
Version:    39
# The dist number is the version here, it is intentionally not repeated in the release
%global dist %nil
Release:    %autorelease
Summary:    A package to obsolete retired packages

# This package has no actual content; there is nothing to license.
License:    LicenseRef-Fedora-Public-Domain
URL:        https://docs.fedoraproject.org/en-US/packaging-guidelines/#renaming-or-replacing-existing-packages
BuildArch:  noarch

Source0:    README

# ===============================================================================
# Skip down below these convenience macros
%define obsolete_ticket() %{lua:
    local ticket = rpm.expand('%1')

    -- May need to declare the master structure
    if type(obs) == 'nil' then
        obs = {}
    end

    if ticket == '%1' then
        rpm.expand('%{error:No ticket provided to obsolete_ticket}')
    end

    if ticket == 'Ishouldfileaticket' then
        ticket = nil
    end

    -- Declare a new set of obsoletes
    local index = #obs+1
    obs[index] = {}
    obs[index].ticket = ticket
    obs[index].list = {}
}

%define obsolete() %{lua:
    local pkg = rpm.expand('%1')
    local ver = rpm.expand('%2')
    local pkg_
    local ver_
    local i
    local j

    if pkg == '%1' then
        rpm.expand('%{error:No package name provided to obsolete}')
    end
    if ver == '%2' then
        rpm.expand('%{error:No version provided to obsolete}')
    end

    if not string.find(ver, '-') then
        rpm.expand('%{error:You must provide a version-release, not just a version.}')
    end

    print('Obsoletes: ' .. pkg .. ' < ' .. ver)

    -- Check if the package wasn't already obsoleted
    for i = 1,#obs do
        for j = 1,#obs[i].list do
            pkg_, ver_ = table.unpack(obs[i].list[j])
            if pkg == pkg_ then
                rpm.expand('%{error:' .. pkg ..' obsoleted multiple times (' .. ver_ .. ' and ' .. ver ..').}')
            end
        end
    end

    -- Append this obsolete to the last set of obsoletes in the list
    local list = obs[#obs].list
    list[#list+1] = {pkg, ver}
}

%define list_obsoletes %{lua:
    local i
    local j
    for i = 1,#obs do
        for j = 1,#obs[i].list do
            pkg, ver = table.unpack(obs[i].list[j])
            print('  ' .. pkg .. ' < ' .. ver .. '\\n')
        end
        if obs[i].ticket == nil then
            print('  (No ticket was provided!)\\n\\n')
        else
            print('  (See ' .. obs[i].ticket .. ')\\n\\n')
        end
    end
}

# ===============================================================================
# Add calls to the obsolete_ticket and obsolete macros below, along with a note
# indicating the Fedora version in which the entries can be removed. This is
# generally three releases beyond whatever release Rawhide is currently. The
# macros make this easy, and will automatically update the package description.

# A link with information is important. Please don't add things here
# without having a link to a ticket in bugzilla, a link to a package
# retirement commit, or something similar.

# All Obsoletes: entries MUST be versioned (including the release),
# with the version being higher (!)
# than the last version-release of the obsoleted package.
# This allows the package to return to the distribution later.
# The best possible thing to do is to find the last version-release
# which was in the distribution, add one to the release,
# and add that version without using a dist tag.
# This allows a rebuild with a bumped Release: to be installed.

# Template:
# Remove in F40
# %%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1234567
# %%obsolete foo 3.5-7

# Remove in F38
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=2126661
%obsolete perl-Verilog-CodeGen 0.9.4-39
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=2046787
%obsolete opencolorio1 1.1.1-5

# Remove in F39
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=2126677
%obsolete perl-File-Inplace 0.20-32
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=2126679
%obsolete perl-Lingua-EN-Fathom 1.22-12
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=2126682
%obsolete perl-Lingua-EN-Syllable 0.30-19
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=2101838
%obsolete publican 4.3.2-24

# Remove in F39
# Removed packages with broken dependencies on Python 3.10
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=2117256
%obsolete ansible-test 2.9.27-5
%obsolete bugzilla2fedmsg 1.0.0-8
%obsolete chavier 0.7.0-23
%obsolete commissaire-client 0.0.6-18
%obsolete datanommer 0.2.0-25
%obsolete expliot 0.9.6-6
%obsolete fapolicyd-dnf-plugin 1.1.3-2
%obsolete hyperkitty 1.3.5-2
%obsolete ipsilon-authfas 2.1.0-24
%obsolete ipsilon-persona 2.1.0-24
%obsolete magic-wormhole 0.12.0-8
%obsolete mailman3 3.3.4-7
%obsolete mkdocs 1.2.3-3
%obsolete mkdocs-alabaster 0.8.0-8
%obsolete mkdocs-bootstrap 1.1-9
%obsolete mkdocs-bootswatch 1.1-7
%obsolete mkdocs-cinder 1.0.3-8
%obsolete mkdocs-docs 1.2.3-3
%obsolete mkdocs-markdownextradata-plugin 0.2.5-3
%obsolete mkdocs-material 5.0.2-8
%obsolete nmstate-plugin-ovsdb 2.0.0-2
%obsolete noggin-tests 0.0.1^git20210323.3b487ed-4
%obsolete nudepy 0.5.0-8
%obsolete paternoster 3.3.0-8
%obsolete percol 0.1.1-0.24
%obsolete postorius 1.3.6-3
%obsolete python-proteus 4.0.2-18
%obsolete python3-ECPy 0.10.0-13
%obsolete python3-PyPAM 0.5.0-51
%obsolete python3-aiomodbus 0.3.2-6
%obsolete python3-aioopenssl 0.5.1-6
%obsolete python3-aiosasl 0.4.1-7
%obsolete python3-altgraph 0.17-8
%obsolete python3-angr 9.0.6885-6
%obsolete python3-argh 0.26.1-23
%obsolete python3-asyncio-dgram 1.1.1-6
%obsolete python3-august 0.25.2-6
%obsolete python3-autoclasstoc 1.3.0-2
%obsolete python3-avocado-plugins-glib 82.0-6
%obsolete python3-avocado-plugins-loader-yaml 82.0-6
%obsolete python3-bigsuds 1.0.6-22
%obsolete python3-blackbird 0.5-6
%obsolete python3-bna 5.0.1-5
%obsolete python3-bodhi 5.7.5-2
%obsolete python3-brother 1.1.0-3
%obsolete python3-cachez 0.1.2-20
%obsolete python3-calligrabot 1.0.0-3
%obsolete python3-cchardet 2.1.7-6
%obsolete python3-clyent 1.2.2-19
%obsolete python3-cmigemo 0.1.6-24
%obsolete python3-concurrentloghandler 0.9.1-21
%obsolete python3-contextlib2 0.6.0.post1-5
%obsolete python3-cu2qu 1.6.7-7
%obsolete python3-discord 1.7.3-2
%obsolete python3-django-mailman3 1.3.7-3
%obsolete python3-email_reply_parser 0.3.0-20140523git76e9481.MANUAL
%obsolete python3-evic 0.1-0.28
%obsolete python3-ezdxf+all5 0.17.2-2
%obsolete python3-fastapi 0.78.0-3
%obsolete python3-fastapi+all 0.78.0-3
%obsolete python3-fastcache 1.1.0-13
%obsolete python3-fastimport 0.9.13-3
%obsolete python3-first 2.0.2-5
%obsolete python3-google-api-core+grpcgcp 2.8.0-2
%obsolete python3-google-api-core+grpcio-gcp 2.8.0-2
%obsolete python3-googletrans 4.0.0~rc1-8
%obsolete python3-graphene-sqlalchemy 2.3.0-5
%obsolete python3-graphql-server 3.0.0-7
%obsolete python3-graphql-server+aiohttp 3.0.0-7
%obsolete python3-graphql-server+flask 3.0.0-7
%obsolete python3-graphql-server+webob 3.0.0-7
%obsolete python3-hkdf 0.0.3-13
%obsolete python3-insteon 1.0.8-6
%obsolete python3-javabridge 1.0.19-8
%obsolete python3-jaydebeapi 1.2.3-7
%obsolete python3-jpype 1.3.0-3
%obsolete python3-language-server 0.36.2-7
%obsolete python3-libsoc 0.8.2-20
%obsolete python3-libyang 1.0.225-5
%obsolete python3-lrparsing 1.0.16-11
%obsolete python3-luftdaten 0.6.5-2
%obsolete python3-magic-wormhole 0.12.0-8
%obsolete python3-magic-wormhole-mailbox-server 0.4.1-9
%obsolete python3-magic-wormhole-transit-relay 0.2.1-8
%obsolete python3-mkdocs-redirects 1.0.3-5
%obsolete python3-molten 1.0.1-5
%obsolete python3-mox3 1.1.0-6
%obsolete python3-netssh2 0.1.7-13
%obsolete python3-nose-cover3 0.1.0-34
%obsolete python3-nudepy 0.5.0-8
%obsolete python3-ofxparse 0.21-3
%obsolete python3-omnilogic 0.4.5-3
%obsolete python3-opencensus 0.7.13-4
%obsolete python3-opencensus-context 0.7.13-4
%obsolete python3-opencensus-correlation 0.7.13-4
%obsolete python3-opencensus-ext-azure 0.7.13-4
%obsolete python3-opencensus-ext-datadog 0.7.13-4
%obsolete python3-opencensus-ext-dbapi 0.7.13-4
%obsolete python3-opencensus-ext-django 0.7.13-4
%obsolete python3-opencensus-ext-flask 0.7.13-4
%obsolete python3-opencensus-ext-gevent 0.7.13-4
%obsolete python3-opencensus-ext-grpc 0.7.13-4
%obsolete python3-opencensus-ext-httplib 0.7.13-4
%obsolete python3-opencensus-ext-jaeger 0.7.13-4
%obsolete python3-opencensus-ext-logging 0.7.13-4
%obsolete python3-opencensus-ext-mysql 0.7.13-4
%obsolete python3-opencensus-ext-ocagent 0.7.13-4
%obsolete python3-opencensus-ext-postgresql 0.7.13-4
%obsolete python3-opencensus-ext-prometheus 0.7.13-4
%obsolete python3-opencensus-ext-pymongo 0.7.13-4
%obsolete python3-opencensus-ext-pymysql 0.7.13-4
%obsolete python3-opencensus-ext-pyramid 0.7.13-4
%obsolete python3-opencensus-ext-requests 0.7.13-4
%obsolete python3-opencensus-ext-sqlalchemy 0.7.13-4
%obsolete python3-opencensus-ext-threading 0.7.13-4
%obsolete python3-opencensus-ext-zipkin 0.7.13-4
%obsolete python3-parallel-ssh 1.9.1-10
%obsolete python3-pipreqs 0.4.10-5
%obsolete python3-pkgwat 0.13-12
%obsolete python3-pkgwat-api 0.13-12
%obsolete python3-plette 0.2.3-4
%obsolete python3-plette+validation 0.2.3-4
%obsolete python3-plyvel 1.3.0-6
%obsolete python3-power 1.4-25
%obsolete python3-productivity 0.6.0-2
%obsolete python3-profilehooks 1.12.0-6
%obsolete python3-py-gfm 0.1.4-8
%obsolete python3-py4j 0.10.9-10
%obsolete python3-pycha 0.7.0-23
%obsolete python3-pyduofern 0.34.1-6
%obsolete python3-pyls_black 0.4.7-4
%obsolete python3-pymdown-extensions 7.0-7
%obsolete python3-pystalk 0.5.1-11
%obsolete python3-readthedocs-sphinx-ext 2.1.4-5
%obsolete python3-rpm-head-signing 1.7-3
%obsolete python3-sendgrid 3.6.5-18
%obsolete python3-social-auth-core+saml 4.2.0-2
%obsolete python3-sockjs-tornado 1.0.7-5
%obsolete python3-spake2 0.8-13
%obsolete python3-sphinx-panels 0.6.0-3
%obsolete python3-sphinx-testing 1.0.1-13
%obsolete python3-sqlobject 3.9.1-7
%obsolete python3-ssh2-python 0.26.0-2
%obsolete python3-structlog 19.2.0-9
%obsolete python3-thingserver 0.2.1-6
%obsolete python3-txtorcon 21.1.0-3
%obsolete python3-typer-cli 0.0.12-11
%obsolete python3-unicodecsv 0.14.1-27
%obsolete python3-volvooncall 0.8.12-7
%obsolete python3-wand 0.5.5-10
%obsolete python3-whatever 0.6-8
%obsolete python3-xmlrunner 1.7.7-18
%obsolete python3-yarg 0.1.9-17
%obsolete quasselgrep 0.1-0.15
%obsolete renderdoc 1.17-3
%obsolete renderdoc-devel 1.17-3
%obsolete system-config-repo 0-31
%obsolete tryton 5.4.0-9
%obsolete trytond 4.0.4-20
%obsolete trytond-account 4.0.3-18
%obsolete trytond-account-be 4.0.0-18
%obsolete trytond-account-de-skr03 4.0.0-18
%obsolete trytond-account-invoice 4.0.2-18
%obsolete trytond-account-invoice-history 4.0.1-18
%obsolete trytond-account-invoice-line-standalone 4.0.1-18
%obsolete trytond-account-product 4.0.2-18
%obsolete trytond-account-statement 4.0.2-18
%obsolete trytond-account-stock-anglo-saxon 4.0.1-18
%obsolete trytond-account-stock-continental 4.0.1-18
%obsolete trytond-analytic-account 4.0.1-18
%obsolete trytond-analytic-invoice 4.0.1-18
%obsolete trytond-analytic-purchase 4.0.1-18
%obsolete trytond-analytic-sale 4.0.1-18
%obsolete trytond-company 4.0.3-18
%obsolete trytond-company-work-time 4.0.1-18
%obsolete trytond-country 4.0.1-18
%obsolete trytond-currency 4.0.1-18
%obsolete trytond-dashboard 4.0.1-18
%obsolete trytond-google-maps 4.0.2-18
%obsolete trytond-ldap-authentication 4.0.1-18
%obsolete trytond-mysql 4.0.4-20
%obsolete trytond-openoffice 4.0.4-20
%obsolete trytond-party 4.0.2-18
%obsolete trytond-party-siret 4.0.0-18
%obsolete trytond-pgsql 4.0.4-20
%obsolete trytond-product 4.0.1-18
%obsolete trytond-product-cost-fifo 4.0.1-18
%obsolete trytond-product-cost-history 4.0.0-18
%obsolete trytond-product-price-list 4.0.0-18
%obsolete trytond-project 4.0.1-18
%obsolete trytond-project-plan 4.0.1-18
%obsolete trytond-project-revenue 4.0.1-18
%obsolete trytond-purchase 4.0.3-18
%obsolete trytond-purchase-invoice-line-standalone 4.0.0-18
%obsolete trytond-sale 4.0.3-18
%obsolete trytond-sale-opportunity 4.0.1-18
%obsolete trytond-sale-price-list 4.0.0-18
%obsolete trytond-sqlite 4.0.4-20
%obsolete trytond-stock 4.0.3-18
%obsolete trytond-stock-forecast 4.0.0-18
%obsolete trytond-stock-inventory-location 4.0.1-18
%obsolete trytond-stock-location-sequence 4.0.1-18
%obsolete trytond-stock-product-location 4.0.0-18
%obsolete trytond-stock-supply 4.0.1-18
%obsolete trytond-stock-supply-day 4.0.0-18
%obsolete trytond-timesheet 4.0.1-18
%obsolete waiverdb 1.4.0-2
%obsolete waiverdb-cli 1.4.0-2
%obsolete waiverdb-common 1.4.0-2
%obsolete zuul 3.19.1-6
%obsolete zuul-executor 3.19.1-6
%obsolete zuul-fingergw 3.19.1-6
%obsolete zuul-merger 3.19.1-6
%obsolete zuul-migrate 3.19.1-6
%obsolete zuul-scheduler 3.19.1-6
%obsolete zuul-web 3.19.1-6

# Remove in F39
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=2126443
%obsolete elementary-calculator 1.7.2-3
%obsolete elementary-calendar 6.1.1-2
%obsolete elementary-camera 6.2.0-2
%obsolete elementary-capnet-assist 2.4.2-2
%obsolete elementary-code 6.2.0-2
%obsolete elementary-files 6.1.4-2
%obsolete elementary-greeter 6.1.0-2
%obsolete elementary-mail 6.4.0-2
%obsolete elementary-music 5.1.1-5
%obsolete elementary-notifications 6.0.2-2
%obsolete elementary-photos 2.7.5-2
%obsolete elementary-print 0.1.3-9
%obsolete elementary-screenshot-tool 6.0.2-4
%obsolete elementary-settings-daemon 1.2.0-2
%obsolete elementary-shortcut-overlay 1.2.1-4
%obsolete elementary-sideload 6.0.2-3
%obsolete elementary-tasks 6.3.0-2
%obsolete elementary-terminal 6.1.0-2
%obsolete elementary-videos 2.8.4-2
%obsolete elementary-wallpapers 5.4-7
%obsolete gala 6.3.1-4
%obsolete pantheon-agent-geoclue2 1.0.5-4
%obsolete pantheon-agent-polkit 1.0.5-2
%obsolete pantheon-session-settings 35.0-2
%obsolete switchboard 6.0.2-2
%obsolete switchboard-plug-a11y 2.3.0-4
%obsolete switchboard-plug-about 6.1.0-2
%obsolete switchboard-plug-applications 6.0.1-3
%obsolete switchboard-plug-bluetooth 2.3.6-4
%obsolete switchboard-plug-display 2.3.2-3
%obsolete switchboard-plug-keyboard 2.7.0-4
%obsolete switchboard-plug-mouse-touchpad 6.1.0-3
%obsolete switchboard-plug-networking 2.4.3-2
%obsolete switchboard-plug-notifications 2.2.0-4
%obsolete switchboard-plug-onlineaccounts 6.5.0-2
%obsolete switchboard-plug-pantheon-shell 6.3.0-2
%obsolete switchboard-plug-printers 2.2.0-2
%obsolete switchboard-plug-sharing 2.1.5-4
%obsolete switchboard-plug-sound 2.3.1-2
%obsolete wingpanel 3.0.2-5
%obsolete wingpanel-applications-menu 2.10.2-3
%obsolete wingpanel-indicator-bluetooth 2.1.8-3
%obsolete wingpanel-indicator-datetime 2.4.0-3
%obsolete wingpanel-indicator-keyboard 2.4.0-4
%obsolete wingpanel-indicator-network 2.3.3-2
%obsolete wingpanel-indicator-nightlight 2.1.0-4
%obsolete wingpanel-indicator-notifications 6.0.6-2
%obsolete wingpanel-indicator-power 6.1.0-3
%obsolete wingpanel-indicator-session 2.3.0-4
%obsolete wingpanel-indicator-sound 6.0.1-3

# Remove in F39
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=2127275
%obsolete ocaml-uuidm 0.9.7-21
%obsolete ocaml-uuidm-devel 0.9.7-21

# Remove in F39
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=2126391
%obsolete gnome-books 40.0-6

# Remove in F39
# libquvi-0.9.4-16.fc32 blocks upgrades: libquvi-0.9.4-16.fc32.x86_64 requires liblua-5.3.so()(64bit), but none of the providers can be installed
%obsolete_ticket https://src.fedoraproject.org/rpms/libquvi/c/559014b4bf8fcf774f0bb644530b4d1e264219a3?branch=rawhide
%obsolete libquvi 0.9.4-17
%obsolete libquvi-devel 0.9.4-17

# Remove in F39
# cardpeek-0.8.4-15.fc32 blocks upgrades: cardpeek-0.8.4-15.fc32.x86_64 requires liblua-5.3.so()(64bit), but none of the providers can be installed
%obsolete_ticket https://src.fedoraproject.org/rpms/cardpeek/c/7246f90aa6371294d2c0cd8fc14506ac78364afb?branch=rawhide
%obsolete cardpeek 0.8.4-16

# Remove in F39
# python26-2.6.9-22.fc32 blocks upgrades: python26-2.6.9-21.fc31.x86_64 requires libnsl.so.2()(64bit)
%obsolete python26 2.6.9-23

# Remove in F40
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=2160274
%obsolete ocaml-stdint 0.7.2-2

# Remove in F40
# Retired and blocks upgrades.
%obsolete_ticket https://src.fedoraproject.org/rpms/msv/c/d64a3747a979f709029501929c8ffe97be3e4238?branch=rawhide
%obsolete msv-demo 2013.6.1-20
%obsolete msv-javadoc 2013.6.1-20
%obsolete msv-manual 2013.6.1-20
%obsolete msv-msv 2013.6.1-20
%obsolete msv-rngconv 2013.6.1-20
%obsolete msv-xmlgen 2013.6.1-20
%obsolete msv-zstdlib 2013.6.1-20

# Remove in F40
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=2172468
%obsolete python3-clikit 0.6.2-8

# Remove in F40
%obsolete_ticket https://src.fedoraproject.org/rpms/recordmydesktop/c/47b8daab4a403d351f24e068f9c7b5f9fde7fb7d?branch=rawhide
%obsolete recordmydesktop 0.3.8.1-20

# Remove in F41
# TeXLive sometimes just kills off components without notice, so there is no ticket.
# These items were removed with TeXLive 2023 (first in Fedora 39) and have no replacement.
%obsolete texlive-elegantbook svn64122-67
%obsolete texlive-elegantnote svn62989-67
%obsolete texlive-elegantpaper svn62989-67
%obsolete texlive-tablestyles svn34495.0-67
%obsolete texlive-tablestyles-doc svn34495.0-67
%obsolete texlive-pgf-cmykshadings svn52635-67

# This package won't be installed, but will obsolete other packages
Provides: libsolv-self-destruct-pkg()

%description %intro

Currently obsoleted packages:

%list_obsoletes


%prep
%autosetup -c -T
cp %SOURCE0 .


%files
%doc README


%changelog
%autochangelog
