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
Version:    43
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
# First, declare the main Lua structure
%{lua:obs = {}}
%define obsolete_ticket() %{lua:
    local ticket = rpm.expand('%1')

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
# Remove in F43
# %%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1234567
# %%obsolete foo 3.5-7

# Remove in F43
# Retired during F41, prevents upgrade to F41 because it requires libfmt.so.10
%obsolete_ticket https://src.fedoraproject.org/rpms/rstudio/c/67a9644580937f93325961293246e49d79c648c2?branch=rawhide
%obsolete rstudio-common 2024.04.2+764-4
%obsolete rstudio-desktop 2024.04.2+764-4
%obsolete rstudio-server 2024.04.2+764-4

# Remove in F42
# Retired during F39, prevents upgrade to F40 because requires libruby.so.3.2
%obsolete_ticket https://src.fedoraproject.org/rpms/rubygem-byebug/c/245925a225da471c45cc0eae8d499046a6db7800?branch=rawhide
%obsolete rubygem-byebug 11.1.3-6
%obsolete rubygem-pry-byebug 3.6.0-14

# Remove in F42
# Retired during F39, prevents upgrade to F40 because requires rubygem(shoulda-context) with version constraint
%obsolete_ticket https://src.fedoraproject.org/rpms/rubygem-shoulda/c/ad584cb6c828abf0cfba90769186c9b2613fd946?branch=rawhide
%obsolete rubygem-shoulda 3.6.0-15

# Remove in F42
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=2260493
%obsolete perl-Test-Apocalypse 1.006-30

# Remove in F42
%obsolete_ticket https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/LAE5JLO3KYVQVSF776H4QLY6DTAUQHWR/
%obsolete celestia 1.7.0~320231229.git6899839-6
%obsolete celestia-common 1.7.0~320231229.git6899839-6
%obsolete celestia-doc 1.7.0~320231229.git6899839-6
%obsolete celestia-gtk 1.7.0~320231229.git6899839-6
%obsolete celestia-qt 1.7.0~320231229.git6899839-6
%obsolete celestia-data 1.7.0~320231125.gitdb53ae3-4

# Remove in F44
%obsolete_ticket https://src.fedoraproject.org/rpms/workrave/c/630c7e05debe7e25e0ef3e00b060ca7da021db25?branch=rawhide
%obsolete workrave 1.11.0~beta.13-3
%obsolete workrave-cinnamon 1.11.0~beta.13-3
%obsolete workrave-gnome 1.11.0~beta.13-3
%obsolete workrave-gnome-flashback 1.11.0~beta.13-3
%obsolete workrave-mate 1.11.0~beta.13-3
%obsolete workrave-xfce 1.11.0~beta.13-3

# Remove in F43
%obsolete_ticket https://src.fedoraproject.org/rpms/libomxil-bellagio/c/3684f6e28
%obsolete libomxil-bellagio 0.9.3-34
%obsolete libomxil-bellagio-devel 0.9.3-34
%obsolete libomxil-bellagio-test 0.9.3-34
%obsolete_ticket https://src.fedoraproject.org/rpms/guile/c/b148178cb
%obsolete guile 2.0.14-37
%obsolete guile-devel 2.0.14-37

# Retired during F41, obsolete legacy GIMP plugins with dead upstream
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=2307970
%obsolete gimp-save-for-web 0.29.3-20
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=2307966
%obsolete gimp-layer-via-copy-cut 1.6-27
%obsolete gimp-separate+ 0.5.8-35
%obsolete gimp-wavelet-decompose 0-17

# Remove in F43
# Removed packages with broken dependencies on Python 3.12
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=2302853
%obsolete aiodnsbrute 0.3.3-7
%obsolete apostrophe 1:2.6.3-17
%obsolete ccnet 6.1.8-19
%obsolete ccnet-devel 6.1.8-19
%obsolete container-workflow-tool 1.2.0-10
%obsolete copr-distgit-client 0.73-2
%obsolete csound-devel 6.16.2-13
%obsolete csound-java 6.16.2-13
%obsolete deepin-dock-onboard-plugin 5.5.81-2
%obsolete dlrn 0.14.0-16
%obsolete dmlite-dpmhead-domeonly 1.15.2-21
%obsolete dmlite-shell 1.15.2-21
%obsolete esphomeflasher 1.4.0-9
%obsolete fedmod 0.6.6-6
%obsolete fedmsg 1.1.7-7
%obsolete fontdump 1.3.0-30
%obsolete glue 0.13-14
%obsolete gofer 3.0.0-0.22
%obsolete gofer-tools 3.0.0-0.22
%obsolete goobook 3.5-13
%obsolete heat-cfntools 1.4.2-25
%obsolete hgview 1.14.0-15
%obsolete hgview-common 1.14.0-15
%obsolete hgview-curses 1.14.0-15
%obsolete kf5-kapidox 5.111.0-2
%obsolete kismon 1.0.2-12
%obsolete komikku 1.36.0-2
%obsolete mailman3-fedmsg-plugin 0.5-28
%obsolete mkosi14 14-5
%obsolete module-build-service 3.9.2-10
%obsolete onboard 1.4.1-35
%obsolete onboard-data 1.4.1-35
%obsolete oraculum 0.2.4-13
%obsolete oval-graph 1.3.3-10
%obsolete pipenv 2023.2.18-5
%obsolete python-ZConfig-doc 4.1-2
%obsolete python-idna-ssl 1.1.0-22
%obsolete python-limits-doc 3.9.0-3
%obsolete python3-BTrees 5.2-2
%obsolete python3-EvoPreprocess 0.5.0-7
%obsolete python3-GridDataFormats 1.0.1-8
%obsolete python3-SALib 1.4.7-5
%obsolete python3-ZConfig 4.1-2
%obsolete python3-ZConfig+test 4.1-2
%obsolete python3-ZEO 6.0.0-4
%obsolete python3-ZEO+msgpack 6.0.0-4
%obsolete python3-ZEO+uvloop 6.0.0-4
%obsolete python3-ZODB 6.0-2
%obsolete python3-ZODB3 3.11.0-29
%obsolete python3-abrt-container-addon 2.17.6-2
%obsolete python3-adb 1.3.0-16
%obsolete python3-aiomqtt 0.1.3-21
%obsolete python3-amico 1.0.1-30
%obsolete python3-anymarkup 0.8.1-16
%obsolete python3-anymarkup-core 0.8.1-13
%obsolete python3-apply-defaults 0.1.4-15
%obsolete python3-astropy-helpers 4.0.1-13
%obsolete python3-astunparse 1.6.3-15
%obsolete python3-atomic-reactor-koji 3.14.0-8
%obsolete python3-atomic-reactor-metadata 3.14.0-8
%obsolete python3-atomic-reactor-rebuilds 3.14.0-8
%obsolete python3-autoprop 4.1.0-11
%obsolete python3-azure-eventhub 5.11.3-3
%obsolete python3-azure-mgmt-automanage 1.0.0-6
%obsolete python3-azure-mgmt-azurestackhci 6.0.0-9
%obsolete python3-azure-mgmt-dashboard 1.0.0-6
%obsolete python3-azure-mgmt-deploymentmanager 1:0.2.0-13
%obsolete python3-azure-mgmt-fluidrelay 1.0.0-6
%obsolete python3-azure-mgmt-hybridcompute 7.0.0-9
%obsolete python3-azure-mgmt-reservations 1:2.0.0-10
%obsolete python3-bash-kernel 0.9.3-4
%obsolete python3-boututils+mayavi 0.1.10-5
%obsolete python3-case 1.5.3-21
%obsolete python3-catch22 0.4.0-14
%obsolete python3-cle 9.2.39-4
%obsolete python3-colorcet 3.0.1^20221003git809e291-13
%obsolete python3-colorcet+examples 3.0.1^20221003git809e291-10
%obsolete python3-compressed-rtf 1.0.6-3
%obsolete python3-csound 6.16.2-13
%obsolete python3-cython0.29 0.29.35-4
%obsolete python3-datadog 0.44.0-10
%obsolete python3-devicely 1.1.1-11
%obsolete python3-devtools 0.12.2-2
%obsolete python3-django-auth-ldap 4.1.0-9
%obsolete python3-django-pyscss 2.0.2-35
%obsolete python3-djvulibre 0.8.7-5
%obsolete python3-dlrn 0.14.0-16
%obsolete python3-dmlite 1.15.2-21
%obsolete python3-dns-lexicon+ddns 3.13.0-2
%obsolete python3-dns-lexicon+duckdns 3.13.0-2
%obsolete python3-dukpy 0.3-25
%obsolete python3-elpy 1.34.0-11
%obsolete python3-esbonio+test 0.16.4-7
%obsolete python3-eventlet 0.35.1-2
%obsolete python3-f5-icontrol-rest 1.3.16-2
%obsolete python3-f5-sdk 3.0.21-23
%obsolete python3-fdb 2.0.1-11
%obsolete python3-fedmsg 1.1.7-7
%obsolete python3-fedmsg-meta-fedora-infrastructure 0.31.0-13
%obsolete python3-ffmpeg-python 0.2.0-7
%obsolete python3-flake8-docstrings 1.6.0-9
%obsolete python3-flask-basicauth 0.2.0-7
%obsolete python3-flask-htmlmin 2.2.1-5
%obsolete python3-fontdump 1.3.0-30
%obsolete python3-future 0.18.3-11
%obsolete python3-gensim 0.10.0-36
%obsolete python3-gensim-addons 0.10.0-36
%obsolete python3-gensim-test 0.10.0-36
%obsolete python3-gnocchiclient-tests 7.0.7-11
%obsolete python3-gofer 3.0.0-0.22
%obsolete python3-gofer-amqp 3.0.0-0.22
%obsolete python3-gofer-proton 3.0.0-0.22
%obsolete python3-google-cloud-access-approval 1.11.3-2
%obsolete python3-google-cloud-access-context-manager 0.1.16-4
%obsolete python3-google-cloud-api-gateway 1.7.3-2
%obsolete python3-google-cloud-apigee-connect 1.7.1-4
%obsolete python3-google-cloud-appengine-admin 1.9.4-2
%obsolete python3-google-cloud-asset 3.22.0-2
%obsolete python3-google-cloud-automl 2.11.4-2
%obsolete python3-google-cloud-bigquery 3.14.0-4
%obsolete python3-google-cloud-bigquery+bqstorage 3.14.0-4
%obsolete python3-google-cloud-bigquery+geopandas 3.14.0-4
%obsolete python3-google-cloud-bigquery+ipython 3.14.0-4
%obsolete python3-google-cloud-bigquery+tqdm 3.14.0-4
%obsolete python3-google-cloud-bigquery-connection 1.13.2-2
%obsolete python3-google-cloud-bigquery-datatransfer 3.12.1-2
%obsolete python3-google-cloud-bigquery-reservation 1.11.3-2
%obsolete python3-google-cloud-bigquery-storage 2.22.0-4
%obsolete python3-google-cloud-bigquery-storage+fastavro 2.22.0-4
%obsolete python3-google-cloud-bigquery-storage+pandas 2.22.0-4
%obsolete python3-google-cloud-bigquery-storage+pyarrow 2.22.0-4
%obsolete python3-google-cloud-bigtable 2.21.0-2
%obsolete python3-google-cloud-billing 1.11.4-3
%obsolete python3-google-cloud-billing-budgets 1.12.1-3
%obsolete python3-google-cloud-build 3.21.0-2
%obsolete python3-google-cloud-common 1.2.0-4
%obsolete python3-google-cloud-container 2.33.0-2
%obsolete python3-google-cloud-containeranalysis 2.12.4-2
%obsolete python3-google-cloud-data-fusion 1.8.3-2
%obsolete python3-google-cloud-datacatalog 3.11.1-4
%obsolete python3-google-cloud-dataproc 5.7.0-2
%obsolete python3-google-cloud-dataproc-metastore 1.13.0-2
%obsolete python3-google-cloud-debugger-client 1.7.0-3
%obsolete python3-google-cloud-deploy 1.14.0-2
%obsolete python3-google-cloud-dlp 3.13.0-3
%obsolete python3-google-cloud-dms 1.7.2-3
%obsolete python3-google-cloud-domains 1.4.1-4
%obsolete python3-google-cloud-filestore 1.5.0-4
%obsolete python3-google-cloud-firestore 2.13.1-2
%obsolete python3-google-cloud-functions 1.13.3-3
%obsolete python3-google-cloud-iam 2.12.2-2
%obsolete python3-google-cloud-kms 2.19.2-2
%obsolete python3-google-cloud-monitoring 2.19.1-2
%obsolete python3-google-cloud-org-policy 1.8.3-3
%obsolete python3-google-cloud-os-config 1.15.3-2
%obsolete python3-google-cloud-private-ca 1.8.2-3
%obsolete python3-google-cloud-pubsub 2.14.1-5
%obsolete python3-google-cloud-pubsub+libcst 2.14.1-5
%obsolete python3-google-cloud-redis 2.13.2-3
%obsolete python3-google-cloud-shell 1.6.1-4
%obsolete python3-google-cloud-source-context 1.4.3-3
%obsolete python3-google-cloud-spanner 3.40.1-2
%obsolete python3-grabbit 0.2.6-29
%obsolete python3-grafeas 1.8.1-4
%obsolete python3-guizero 1.3.0-7
%obsolete python3-gunicorn+eventlet 21.2.0-5
%obsolete python3-gunicorn+gevent 21.2.0-5
%obsolete python3-gunicorn+setproctitle 21.2.0-5
%obsolete python3-hdmf+zarr 3.14.3-2
%obsolete python3-htmlmin 0.1.12-23
%obsolete python3-hypothesis-fspaths 0.1-19
%obsolete python3-ipdb 0.13.13-7
%obsolete python3-iptools 0.7.0-14
%obsolete python3-j1m.sphinxautozconfig 0.1.0-23
%obsolete python3-jose 3.3.0-30
%obsolete python3-jose+cryptography 3.3.0-30
%obsolete python3-jsonschema-spec 0.2.4-2
%obsolete python3-jupyter-collaboration 1.0.0-4
%obsolete python3-jupyter-server-fileid 0.9.0-3
%obsolete python3-jupyter-sphinx 0.5.3-4
%obsolete python3-jupyter-ydoc 1.0.2-4
%obsolete python3-kaitaistruct 0.10-6
%obsolete python3-limits 3.9.0-3
%obsolete python3-limits+etcd 3.9.0-3
%obsolete python3-limits+memcached 3.9.0-3
%obsolete python3-limits+mongodb 3.9.0-3
%obsolete python3-limits+redis 3.9.0-3
%obsolete python3-limits+rediscluster 3.9.0-3
%obsolete python3-m2crypto 0.41.0^git20240613.3156614-2
%obsolete python3-matplotlib-venn 0.11.9-4
%obsolete python3-maya 0.6.1-11
%obsolete python3-metaextract 1.0.9-5
%obsolete python3-mglob 0.4-43
%obsolete python3-mysql-debug 1.4.6-15
%obsolete python3-nb2plots 0.7.2-4
%obsolete python3-openapi-spec-validator+requests 0.5.7-5
%obsolete python3-openipmi 2.0.32-11
%obsolete python3-openopt 0.5629-14
%obsolete python3-opentelemetry-instrumentation-grpc 1:0.39~b0-27
%obsolete python3-opentelemetry-instrumentation-grpc+instruments 1:0.39~b0-27
%obsolete python3-opentracing 2.4.0-13
%obsolete python3-opentype-sanitizer 9.1.0-12
%obsolete python3-orderedset 2.0.3-12
%obsolete python3-oslo-db 14.1.0-4
%obsolete python3-oslo-db+mysql 14.1.0-4
%obsolete python3-oslo-db-tests 14.1.0-4
%obsolete python3-oslo-service 3.1.1-11
%obsolete python3-oslo-service-tests 3.1.1-11
%obsolete python3-oslo-sphinx 4.18.0-20
%obsolete python3-param 2.0.2-6
%obsolete python3-pep517 0.13.0-6
%obsolete python3-persistent 5.2-2
%obsolete python3-persistent-devel 5.2-2
%obsolete python3-persistent-doc 5.2-2
%obsolete python3-pplpy 0.8.10-2
%obsolete python3-pplpy-devel 0.8.10-2
%obsolete python3-prelude 5.2.0-27
%obsolete python3-preprocess 2.0.0-12
%obsolete python3-primecountpy 0.1.0-14
%obsolete python3-py-gql 0.6.1-15
%obsolete python3-pyct 0.5.0-9
%obsolete python3-pyct+build 0.5.0-9
%obsolete python3-pyct+cmd 0.5.0-9
%obsolete python3-pyfastnoisesimd 0.4.2-13
%obsolete python3-pyhirte 0.4.0-4
%obsolete python3-pykdl 1.5.1-11
%obsolete python3-pyliblo 0.10.0-31
%obsolete python3-pymoc 0.5.0-26
%obsolete python3-pyswarms 1.3.0-23
%obsolete python3-pytest-bdd5 5.0.0-6
%obsolete python3-pytest-cython 0.2.2-2
%obsolete python3-pytest-grpc 0.8.0^20210806git3f21554-15
%obsolete python3-pyvex 9.2.39-4
%obsolete python3-pyvhacd 0.0.2-2
%obsolete python3-r128gain 1.0.7-6
%obsolete python3-ratelimiter 1.2.0-13
%obsolete python3-rdflib-jsonld 0.6.0-10
%obsolete python3-receptor-python-worker 1.4.4-3
%obsolete python3-red-black-tree-mod 1.21-2
%obsolete python3-remctl 3.18-9
%obsolete python3-ruffus 2.8.4-17
%obsolete python3-scripttester 0.1-22
%obsolete python3-scss 1.4.0-4
%obsolete python3-setuptools_scm_git_archive 1.4-5
%obsolete python3-signature-dispatch 1.0.1-8
%obsolete python3-smartcols 0.3.0-21
%obsolete python3-snipeit 1.2-11
%obsolete python3-social-auth-core+openidconnect 4.3.0-9
%obsolete python3-sphinxbase 1:5-0.19
%obsolete python3-sphinxcontrib-applehelp 1.0.2-15
%obsolete python3-sphinxcontrib-jsmath 1.0.1-23
%obsolete python3-sphinxcontrib-openapi 0.7.0-12
%obsolete python3-sphinxcontrib-zopeext 0.4.3-4
%obsolete python3-sphinxext-rediraffe 0.2.7-9
%obsolete python3-sqlalchemy+aioodbc 2.0.35-2
%obsolete python3-sqlalchemy+mssql_pyodbc 2.0.35-2
%obsolete python3-sqlalchemy+postgresql_pg8000 2.0.35-2
%obsolete python3-stompest 2.3.0-17
%obsolete python3-stompest-twisted 2.3.0-17
%obsolete python3-subvertpy 0.10.1-23
%obsolete python3-tdlib 0.9.2-13
%obsolete python3-tdlib-devel 0.9.2-13
%obsolete python3-testinfra 5.3.1-15
%obsolete python3-timeunit 1.1.0-14
%obsolete python3-tmt 1.27.0-2
%obsolete python3-transtats-cli 0.6.0-8
%obsolete python3-trollius 2.1-29
%obsolete python3-tweepy 4.7.0-10
%obsolete python3-tweepy+async 4.7.0-10
%obsolete python3-tweepy+socks 4.7.0-10
%obsolete python3-twitter 3.5-19
%obsolete python3-typed_ast 1.5.5-3
%obsolete python3-typer+all 0.11.1-2
%obsolete python3-uamqp 1.6.5-2
%obsolete python3-vagrantpy 0.6.0-14
%obsolete python3-vecrec 0.3.1-18
%obsolete python3-vitrageclient 4.8.0-2
%obsolete python3-webpy 0.62-11
%obsolete python3-woffTools 0.1-0.40
%obsolete python3-wsaccel 0.6.6-4
%obsolete python3-wtforms-sqlalchemy 0.3.0-8
%obsolete python3-y-py 0.6.0-5
%obsolete python3-ypy-websocket 0.8.4-4
%obsolete python3-zanata-client 1.5.3-19
%obsolete python3-zanata2fedmsg 0.2-30
%obsolete python3-zbase32 1.1.5-33
%obsolete python3-zdaemon 4.2.0-27
%obsolete python3-zodbpickle 3.2-3
%obsolete python3-zope-fixers 1.1.2-33
%obsolete python3-zopeundo 6.0-6
%obsolete qpid-dispatch-console 1.19.0-10
%obsolete qpid-dispatch-router 1.19.0-10
%obsolete receptor 1.4.4-3
%obsolete receptorctl 1.4.4-3
%obsolete ruff-lsp 0.0.53-2
%obsolete tmt-all 1.27.0-2
%obsolete tmt-provision-beaker 1.27.0-2
%obsolete tmt-provision-container 1.27.0-2
%obsolete tmt-provision-virtual 1.27.0-2
%obsolete tmt-report-html 1.27.0-2
%obsolete tmt-report-junit 1.27.0-2
%obsolete tmt-report-polarion 1.27.0-2
%obsolete tmt-report-reportportal 1.27.0-2
%obsolete woffTools 0.1-0.40

%obsolete_ticket https://src.fedoraproject.org/rpms/writer2latex/c/74f42c8fcd2009bc23b2d0ff7005dda9afa50027
%obsolete libreoffice-writer2latex 1.0.2-41

%obsolete_ticket https://src.fedoraproject.org/rpms/torque/c/5f8d64fc9a899f4b94e63685a29f4cc95ef2f829
%obsolete torque 6.1.3-14
%obsolete torque-libs 6.1.3-14

%obsolete_ticket https://src.fedoraproject.org/rpms/kf5-kitinerary/c/0d6cd68645c84c27a9aef46f8dd88056396eae0f
%obsolete kf5-kitinerary 23.08.5-7
%obsolete kf5-kitinerary-devel 23.08.5-7

%obsolete_ticket https://src.fedoraproject.org/rpms/gnome-online-miners/c/aed3cac7c83e5f4787a7cf60eda4a8aa8fe47c59
%obsolete gnome-online-miners 3.34.0-12

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
