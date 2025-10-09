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
Version:    44
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
%obsolete esphomeflasher 1.4.0-9
%obsolete fedmod 0.6.6-6
%obsolete fedmsg 1.1.7-7
%obsolete fontdump 1.3.0-30
%obsolete glue 0.13-14
%obsolete gofer 3.0.0-0.22
%obsolete gofer-tools 3.0.0-0.22
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
%obsolete prelude-correlator 5.2.0-14
%obsolete python-ZConfig-doc 4.1-2
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
%obsolete python3-boututils+mayavi 0.1.10-5
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
%obsolete python3-ipdb 0.13.13-7
%obsolete python3-j1m.sphinxautozconfig 0.1.0-23
%obsolete python3-jose 3.3.0-30
%obsolete python3-jose+cryptography 3.3.0-30
%obsolete python3-jsonschema-spec 0.2.4-2
%obsolete python3-jupyter-collaboration 1.0.0-4
%obsolete python3-jupyter-server-fileid 0.9.0-3
%obsolete python3-jupyter-ydoc 1.0.2-4
%obsolete python3-kaitaistruct 0.10-6
%obsolete python3-limits 3.9.0-3
%obsolete python3-limits+etcd 3.9.0-3
%obsolete python3-limits+memcached 3.9.0-3
%obsolete python3-limits+mongodb 3.9.0-3
%obsolete python3-limits+redis 3.9.0-3
%obsolete python3-limits+rediscluster 3.9.0-3
%obsolete python3-matplotlib-venn 0.11.9-4
%obsolete python3-maya 0.6.1-11
%obsolete python3-metaextract 1.0.9-5
%obsolete python3-mglob 0.4-43
%obsolete python3-mysql-debug 1.4.6-15
%obsolete python3-openapi-spec-validator+requests 0.5.7-5
%obsolete python3-openipmi 2.0.32-11
%obsolete python3-openopt 0.5629-14
%obsolete python3-opentelemetry-instrumentation-grpc 1:0.39~b0-27
%obsolete python3-opentelemetry-instrumentation-grpc+instruments 1:0.39~b0-27
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
%obsolete python3-prelude-correlator 5.2.0-14
%obsolete python3-preludedb 5.2.0-14
%obsolete python3-preprocess 2.0.0-12
%obsolete python3-primecountpy 0.1.0-14
%obsolete python3-py-gql 0.6.1-15
%obsolete python3-pyct 0.5.0-9
%obsolete python3-pyct+build 0.5.0-9
%obsolete python3-pyct+cmd 0.5.0-9
%obsolete python3-pyfastnoisesimd 0.4.2-13
%obsolete python3-pyhirte 0.4.0-4
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
%obsolete python3-red-black-tree-mod 1.21-2
%obsolete python3-remctl 3.18-9
%obsolete python3-ruffus 2.8.4-17
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
%obsolete python3-zodbpickle 3.2-3
%obsolete python3-zope-fixers 1.1.2-33
%obsolete python3-zopeundo 6.0-6
%obsolete qpid-dispatch-console 1.19.0-10
%obsolete qpid-dispatch-router 1.19.0-10
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

%obsolete_ticket https://src.fedoraproject.org/rpms/dmraid/c/2a27f40357e52d5497a0245b05624ce37b8474e6
%obsolete dmraid 1.0.0.rc16-61
%obsolete dmraid-devel 1.0.0.rc16-61
%obsolete dmraid-events 1.0.0.rc16-61
%obsolete dmraid-events-logwatch 1.0.0.rc16-61
%obsolete dmraid-libs 1.0.0.rc16-61

# Removed packages with broken dependencies on Python 3.13
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=2373699
%obsolete artifacts 0.0.20240518-5
%obsolete asv 0.5.1-17
%obsolete bandit 1.8.2-3
%obsolete bst-external 0.30.0-10
%obsolete cantera-devel 3.1.0-3
%obsolete cantoolz 3.7.0-24
%obsolete cfn-lint 1.36.0-2
%obsolete cfn-lint+full 1.36.0-2
%obsolete cfn-lint+graph 1.36.0-2
%obsolete cfn-lint+junit 1.36.0-2
%obsolete cfn-lint+sarif 1.36.0-2
%obsolete check-manifest 0.50-3
%obsolete cinch 1.4.0-23
%obsolete coapthon3 1.0.1-23
%obsolete cranc 1.1.0-20
%obsolete credslayer 0.1.2-18
%obsolete dcrpm 0.6.3-14
%obsolete dingz 0.5.0-11
%obsolete dmlite-dpm-tester 1.15.2-22
%obsolete dmlite-dpmhead-domeonly 1.15.2-22
%obsolete dmlite-shell 1.15.2-22
%obsolete dnsgen 1.0.4-17
%obsolete dput-ng 1.21-24
%obsolete fedora-business-cards 2.3.0-13
%obsolete fedscm-admin 1.1.7-10
%obsolete gfal2-util-scripts 1.9.0-3
%obsolete goobook 3.5-15
%obsolete hashid 3.1.4-24
%obsolete hypershell 2.7.0-2
%obsolete imagehash-demo 4.3.2-5
%obsolete ioc-writer 0.3.3-23
%obsolete ipa-hcc-server 0.18-4
%obsolete ipgetter2 1.1.11-17
%obsolete kerberoast 0.1.4-16
%obsolete ldapdomaindump 0.9.3-19
%obsolete ldeep 1.0.9-16
%obsolete lecm 0.0.7-28
%obsolete linode-cli 5.35.0-8
%obsolete linux-thermaltake-rgb 0.2.0-21
%obsolete livereload 2.6.3-17
%obsolete metrics2mqtt 0.1.18-17
%obsolete minidump 0.0.24-3
%obsolete mirrormanager2 1.0.0-11
%obsolete mirrormanager2-backend 1.0.0-11
%obsolete mirrormanager2-crawler 1.0.0-11
%obsolete mirrormanager2-lib 1.0.0-11
%obsolete mirrormanager2-statistics 1.0.0-11
%obsolete mom 0.6.4-12
%obsolete mu 1.2.0-21
%obsolete mygnuhealth 1.0.5-13
%obsolete mystrom 2.0.0-16
%obsolete netstat-monitor 1.1.3-32
%obsolete neuron 8.2.6-3
%obsolete neuron-devel 8.2.6-3
%obsolete neuron-mpich 8.2.6-3
%obsolete neuron-mpich-devel 8.2.6-3
%obsolete neuron-openmpi 8.2.6-3
%obsolete neuron-openmpi-devel 8.2.6-3
%obsolete nik4 1.7.0-6
%obsolete nova-agent 2.1.25-12
%obsolete odcs 0.9.0-2
%obsolete odcs-client 0.9.0-2
%obsolete pag 0.8-24
%obsolete pagure 5.14.1-7
%obsolete pagure-ci 5.14.1-7
%obsolete pagure-ev 5.14.1-7
%obsolete pagure-loadjson 5.14.1-7
%obsolete pagure-logcom 5.14.1-7
%obsolete pagure-milters 5.14.1-7
%obsolete pagure-mirror 5.14.1-7
%obsolete pagure-theme-chameleon 5.14.1-7
%obsolete pagure-theme-pagureio 5.14.1-7
%obsolete pagure-theme-srcfpo 5.14.1-7
%obsolete pagure-web-apache-httpd 5.14.1-7
%obsolete pagure-web-nginx 5.14.1-7
%obsolete pagure-webhook 5.14.1-7
%obsolete parsero 0.81-34
%obsolete past-time 0.3.1-3
%obsolete pdc-client 1.8.0-36
%obsolete pdfposter 0.7.post1-25
%obsolete poezio 0.14-13
%obsolete poezio-doc 0.14-13
%obsolete postgresql15-contrib 15.8-2
%obsolete postgresql15-plpython3 15.8-2
%obsolete postgresql15-test 15.8-2
%obsolete postgresql15-upgrade 15.8-2
%obsolete postgresql15-upgrade-devel 15.8-2
%obsolete prewikka 5.2.0-19
%obsolete pwncat 0.1.0-18
%obsolete pypykatz 0.3.15-16
%obsolete pysubnettree 0.35-12
%obsolete python-hudman-doc 9.0.0-11
%obsolete python-idna-ssl 1.1.0-24
%obsolete python-jack-client 0.5.2-17
%obsolete python-mizani-doc 0.13.5-2
%obsolete python-pkginfo2-doc 30.0.0-7
%obsolete python-play-scraper 0.6.0-21
%obsolete python-ufl-demo 2019.1.0-25
%obsolete python-ufl-test 2019.1.0-25
%obsolete python3-ATpy 0.9.7-44
%obsolete python3-AWSIoTPythonSDK 1.4.9-17
%obsolete python3-GeographicLib 2.0-3
%obsolete python3-Naked 0.1.31-29
%obsolete python3-PyDrive2 1.20.0-3
%obsolete python3-PyLEMS 0.6.8-2
%obsolete python3-PyLink 0.3.2-33
%obsolete python3-TGScheduler 1.7.0-33
%obsolete python3-XStatic 1.0.1-37
%obsolete python3-XStatic-Angular 1:1.5.8.0-29
%obsolete python3-XStatic-Angular-Bootstrap 2.2.0.0-28
%obsolete python3-XStatic-Angular-Gettext 2.1.0.2-33
%obsolete python3-XStatic-Angular-lrdragndrop 1.0.2.2-34
%obsolete python3-XStatic-Hogan 2.0.0.2-36
%obsolete python3-XStatic-JQuery-Migrate 1.2.1.1-35
%obsolete python3-XStatic-JQuery-TableSorter 2.14.5.1-35
%obsolete python3-XStatic-JQuery-quicksearch 2.0.3.2-3
%obsolete python3-XStatic-JSEncrypt 2.3.1.1-27
%obsolete python3-XStatic-Jasmine 2.4.1.1-27
%obsolete python3-XStatic-Magic-Search 0.2.5.1-31
%obsolete python3-XStatic-QUnit 1.14.0.2-35
%obsolete python3-XStatic-Rickshaw 1.5.0.0-37
%obsolete python3-XStatic-Spin 1.2.5.2-36
%obsolete python3-XStatic-roboto-fontface 0.5.0.0-30
%obsolete python3-XStatic-smart-table 1.4.13.2-27
%obsolete python3-XStatic-termjs 0.0.7.0-27
%obsolete python3-accuweather 0.0.11-17
%obsolete python3-adafruit-pureio 1.1.10-9
%obsolete python3-adapt 1.0.0-11
%obsolete python3-adjustText 1.3.0-3
%obsolete python3-afsapi 0.2.8-3
%obsolete python3-aioasuswrt 1.4.0-12
%obsolete python3-aiocmd 0.1.5-17
%obsolete python3-aioeafm 1.0.0-17
%obsolete python3-aioesphomeapi 15.0.0-5
%obsolete python3-aioflo 0.4.2-15
%obsolete python3-aiogqlc 1.0.4-17
%obsolete python3-aiohomekit 0.2.60-17
%obsolete python3-aiohttp-sse-client 0.2.0-17
%obsolete python3-aiohue 2.2.0-19
%obsolete python3-aioiotprov 0.0.7-16
%obsolete python3-aiokafka 0.12.0-3
%obsolete python3-aiolifx 0.8.9-10
%obsolete python3-aiomultiprocess 0.9.1-3
%obsolete python3-aionotion 2.0.3-17
%obsolete python3-aiopg 1.3.4-11
%obsolete python3-aiorestapi 0.1.1-19
%obsolete python3-aiosecretsdump 0.0.2-16
%obsolete python3-aiosmb 0.2.35-15
%obsolete python3-aiosnmp 0.5.0-13
%obsolete python3-aiowinreg 0.0.12-3
%obsolete python3-airspeed 0.6.0-7
%obsolete python3-ajpy 0.0.5-19
%obsolete python3-alsaaudio 0.10.0-6
%obsolete python3-amply 0.1.6-10
%obsolete python3-ana 0.06-20
%obsolete python3-ansicolors 1.1.8-29
%obsolete python3-ansiwrap 0.8.4-20
%obsolete python3-anyconfig 0.13.0-12
%obsolete python3-aresponses 3.0.0-5
%obsolete python3-arm-preprocessing 0.2.5-2
%obsolete python3-astor 0.8.1-25
%obsolete python3-astral 3.2-9
%obsolete python3-async-upnp-client 0.14.15-17
%obsolete python3-auth-credential 1.1-13
%obsolete python3-autograd 1.8.0-3
%obsolete python3-autograd+scipy 1.8.0-3
%obsolete python3-avocado 92.3-5
%obsolete python3-avocado-plugins-golang 92.3-5
%obsolete python3-avocado-plugins-output-html 92.3-5
%obsolete python3-avocado-plugins-result-upload 92.3-5
%obsolete python3-avocado-plugins-resultsdb 92.3-5
%obsolete python3-avocado-plugins-varianter-cit 92.3-5
%obsolete python3-avocado-plugins-varianter-pict 92.3-5
%obsolete python3-avocado-plugins-varianter-yaml-to-mux 92.3-5
%obsolete python3-aws-sam-translator 1.98.0-2
%obsolete python3-aws-xray-sdk 2.14.0-9
%obsolete python3-awsiotsdk 1.22.0-3
%obsolete python3-baluhn 0.1.2-23
%obsolete python3-barbicanclient 7.0.0-4
%obsolete python3-bash-kernel 0.9.3-6
%obsolete python3-betamax-matchers 0.4.0-25
%obsolete python3-betamax-serializers 0.2.0-25
%obsolete python3-bioframe 0.8.0-4
%obsolete python3-bluepyopt 1.14.11-4
%obsolete python3-brial 1.2.12-8
%obsolete python3-cachy 0.3.0-21
%obsolete python3-cantera 3.1.0-3
%obsolete python3-case 1.5.3-23
%obsolete python3-chalice 1.31.2-4
%obsolete python3-check-manifest 0.50-3
%obsolete python3-chirpstack-api 3.9.4-15
%obsolete python3-ci-info 0.3.0-3
%obsolete python3-click-help-colors 0.9.1-14
%obsolete python3-cliff-tablib 1.1-38
%obsolete python3-cloudant 2.15.0-14
%obsolete python3-coapthon3 1.0.1-23
%obsolete python3-colorthief 0.2.1-7
%obsolete python3-commandparse 1.0.8-17
%obsolete python3-compal 0.2.0-16
%obsolete python3-connect-box 0.4.0-5
%obsolete python3-coronavirus 1.1.1-16
%obsolete python3-cradox 2.1.0-27
%obsolete python3-crcelk 1.3-23
%obsolete python3-credslayer 0.1.2-18
%obsolete python3-cx-oracle 8.3.0-12
%obsolete python3-cxxfilt 0.2.0-19
%obsolete python3-cyipopt 1.5.0-4
%obsolete python3-cyipopt-tests 1.5.0-4
%obsolete python3-cysignals 1.11.4-7
%obsolete python3-cysignals-devel 1.11.4-7
%obsolete python3-daikin 2.4.0-17
%obsolete python3-danfossair 0.1.0-18
%obsolete python3-databases 0.9.0-5
%obsolete python3-databases+aiomysql 0.9.0-5
%obsolete python3-databases+aiopg 0.9.0-5
%obsolete python3-databases+aiosqlite 0.9.0-5
%obsolete python3-databases+asyncmy 0.9.0-5
%obsolete python3-databases+asyncpg 0.9.0-5
%obsolete python3-databases+mysql 0.9.0-5
%obsolete python3-databases+postgresql 0.9.0-5
%obsolete python3-databases+sqlite 0.9.0-5
%obsolete python3-dateutils 0.6.8-18
%obsolete python3-datrie 0.8.2-30
%obsolete python3-dbutils 3.0.3-9
%obsolete python3-deconz 76-16
%obsolete python3-designateclient 6.1.0-3
%obsolete python3-designateclient-tests 6.1.0-3
%obsolete python3-devolo-home-control-api 0.16.0-18
%obsolete python3-dfdatetime 20240504-3
%obsolete python3-dictdumper 0.8.4-14
%obsolete python3-didl-lite 1.2.5-18
%obsolete python3-dingz 0.5.0-11
%obsolete python3-distro-info 0.18-24
%obsolete python3-django-contrib-comments 2.0.0-18
%obsolete python3-django-prometheus 2.1.0-15
%obsolete python3-django-threadedcomments 1.2-28
%obsolete python3-django4.2 4.2.23-2
%obsolete python3-django5 5.1.11-2
%obsolete python3-dlib 19.24.8-4
%obsolete python3-dmlite 1.15.2-22
%obsolete python3-dnsgen 1.0.4-17
%obsolete python3-dnslib 0.9.21-11
%obsolete python3-dnspython 2.7.0-5
%obsolete python3-dnspython+dnssec 2.7.0-5
%obsolete python3-dnspython+doh 2.7.0-5
%obsolete python3-dnspython+doq 2.7.0-5
%obsolete python3-dnspython+idna 2.7.0-5
%obsolete python3-dnspython+trio 2.7.0-5
%obsolete python3-docx 1.1.2-5
%obsolete python3-dput 1.21-24
%obsolete python3-dtfabric 0.0.20230520-11
%obsolete python3-earthpy 0.9.4-14
%obsolete python3-easyco 0.2.3-17
%obsolete python3-edimax 0.2.1-16
%obsolete python3-editdistance 0.8.1-5
%obsolete python3-elephant 1.1.1-6
%obsolete python3-enrich 1.2.7-17
%obsolete python3-enturclient 0.2.1-17
%obsolete python3-epi 0.2.1-14
%obsolete python3-epson-projector 0.2.3-16
%obsolete python3-epub 0.5.2-37
%obsolete python3-esbonio+dev 1.0.0b3-5
%obsolete python3-esbonio+typecheck 1.0.0b3-5
%obsolete python3-etelemetry 0.3.1-2
%obsolete python3-exiv2 0.12.0-5
%obsolete python3-fedora 1.1.1-15
%obsolete python3-fedora-flask 1.1.1-15
%obsolete python3-ffmpeg-python 0.2.0-9
%obsolete python3-fiat 2019.1.0-24
%obsolete python3-firkin 0.02-46
%obsolete python3-flann 1.9.2-12
%obsolete python3-flask-xml-rpc 0.1.2-35
%obsolete python3-formulaic 1.1.1-3
%obsolete python3-formulaic+arrow 1.1.1-3
%obsolete python3-formulaic+calculus 1.1.1-3
%obsolete python3-friendlyloris 1.0.1-18
%obsolete python3-fuzzywuzzy 0.18.0-19
%obsolete python3-gabbi 2.7.2-10
%obsolete python3-gammu 3.2.4-14
%obsolete python3-gear 0.16.0-8
%obsolete python3-gekitchen 0.2.19-16
%obsolete python3-genty 1.3.2-24
%obsolete python3-geoplot 0.5.1-14
%obsolete python3-gevent-eventemitter 2.1-18
%obsolete python3-gfal2 1.13.0-3
%obsolete python3-gfal2-util 1.9.0-3
%obsolete python3-gilt 1.2.2-13
%obsolete python3-gios 0.1.4-18
%obsolete python3-git-url-parse 1.2.2-28
%obsolete python3-glances-api 0.2.0-24
%obsolete python3-gphoto2 2.0.0-22
%obsolete python3-graphql-relay 3.2.0-11
%obsolete python3-grip 4.6.2-3
%obsolete python3-habitipy 0.3.0-16
%obsolete python3-hass-data-detective 2.4-16
%obsolete python3-hatasmota 0.7.3-7
%obsolete python3-haversion 24.6.1-3
%obsolete python3-hdate 0.9.11-17
%obsolete python3-hdf5storage 0.1.18-17
%obsolete python3-hgdistver 0.25-32
%obsolete python3-hikvision 2.0.3-16
%obsolete python3-hokuyoaist 3.0.2-56
%obsolete python3-hole 0.9.0-2
%obsolete python3-homeconnect 0.6.3-17
%obsolete python3-homeworks 0.0.6-16
%obsolete python3-hstspreload 2025.1.1-3
%obsolete python3-hudman 9.0.0-11
%obsolete python3-hypercorn+uvloop 0.17.3-8
%obsolete python3-hypershell+postgres 2.7.0-2
%obsolete python3-hypothesis-fspaths 0.1-21
%obsolete python3-imagehash 4.3.2-5
%obsolete python3-instant 2016.1.0-32
%obsolete python3-intern 1.4.2-2
%obsolete python3-ipahcc 0.18-4
%obsolete python3-ipahcc+server 0.18-4
%obsolete python3-ipgetter2 1.1.11-17
%obsolete python3-iptools 0.7.0-16
%obsolete python3-iso-639 0.4.5-30
%obsolete python3-itanium_demangler 1.1-10
%obsolete python3-janus 1.2.0-2
%obsolete python3-javalang 0.13.0-16
%obsolete python3-javaobj 0.4.4-3
%obsolete python3-jenkins 1.8.2-7
%obsolete python3-jenkins-job-builder 1:6.4.2-3
%obsolete python3-jschema-to-python 1.2.3-19
%obsolete python3-json2table 1.1.5-24
%obsolete python3-jsonpath-rw-ext 1.2.2-17
%obsolete python3-jsons 1.5.0-14
%obsolete python3-junit-xml 1.9^20200222gitba89b41-21
%obsolete python3-jupyter-sphinx 0.5.3-6
%obsolete python3-keepassxc-browser 0.1.8-12
%obsolete python3-kerberoast 0.1.4-16
%obsolete python3-kismet-rest 2019.5.2-17
%obsolete python3-korean-lunar-calendar 0.2.1-17
%obsolete python3-lazy-ops 0.2.0-18
%obsolete python3-ldapdomaindump 0.9.3-19
%obsolete python3-ldappool 3.0.0-14
%obsolete python3-ldeep 1.0.9-16
%obsolete python3-lfpy 2.3.2-6
%obsolete python3-libNeuroML 0.6.5-4
%obsolete python3-libfreenect 0.7.0-15
%obsolete python3-libnl3 3.11.0-4
%obsolete python3-linkheader 0.4.3-18
%obsolete python3-livereload 2.6.3-17
%obsolete python3-lqrt 0.3.3-11
%obsolete python3-m2crypto 0.41.0^git20240613.3156614-2
%obsolete python3-m2r 0.3.1-10
%obsolete python3-magnumclient 4.7.0-3
%obsolete python3-magnumclient-tests 4.7.0-3
%obsolete python3-makeelf 0.3.2-19
%obsolete python3-markups 4.0.0-3
%obsolete python3-marshmallow-enum 1.5.1-19
%obsolete python3-masscan 0.1.6-18
%obsolete python3-messaging 1.2-13
%obsolete python3-metno 0.8.1-16
%obsolete python3-metrics2mqtt 0.1.18-17
%obsolete python3-mido 1.2.9-23
%obsolete python3-migrate 0.13.0-21
%obsolete python3-minidump 0.0.24-3
%obsolete python3-mizani 0.13.5-2
%obsolete python3-mne 1.9.0-4
%obsolete python3-mne-bids 0.16.0-13
%obsolete python3-mne-bids+full 0.16.0-13
%obsolete python3-moksha-common 1.2.5-36
%obsolete python3-moksha-hub 1.5.17-26
%obsolete python3-mongoquery 1.4.2-10
%obsolete python3-mpd 0.2.1-43
%obsolete python3-mrcrowbar 0.8.0-17
%obsolete python3-msldap 0.3.26-15
%obsolete python3-mutatormath 3.0.1-15
%obsolete python3-mystrom 2.0.0-16
%obsolete python3-nanoid 2.0.0-18
%obsolete python3-natlas-libnmap 0.7.1-18
%obsolete python3-nb2plots 0.7.2-6
%obsolete python3-ndeflib 0.3.3-4
%obsolete python3-ndg_httpsclient 0.5.1-24
%obsolete python3-neatdend 0.9.2-22
%obsolete python3-nessus-file-reader 0.2.0-19
%obsolete python3-netdata 0.2.0-18
%obsolete python3-netpyne 1.0.7-6
%obsolete python3-network-runner 0.3.6-17
%obsolete python3-neurodsp 2.3.0-3
%obsolete python3-neurom 4.0.4-4
%obsolete python3-neurom+plotly 4.0.4-4
%obsolete python3-neuron 8.2.6-3
%obsolete python3-neuron-mpich 8.2.6-3
%obsolete python3-neuron-openmpi 8.2.6-3
%obsolete python3-neurosynth 0.3.8-17
%obsolete python3-neurotune 0.2.6-9
%obsolete python3-nfcpy 1.0.4-3
%obsolete python3-niaarm 0.4.1-2
%obsolete python3-niaarmts 0.2.0-3
%obsolete python3-nilearn 0.11.1-4
%obsolete python3-nipype 1.10.0-3
%obsolete python3-nipype+data 1.10.0-3
%obsolete python3-nipype+duecredit 1.10.0-3
%obsolete python3-nipype+nipy 1.10.0-3
%obsolete python3-nipype+pybids 1.10.0-3
%obsolete python3-nipype+ssh 1.10.0-3
%obsolete python3-nose 1.3.7-63
%obsolete python3-nose-testconfig 0.10-36
%obsolete python3-nose-timer 1.0.0-17
%obsolete python3-nptyping 2.5.0-3
%obsolete python3-nrf24 1.1.1-16
%obsolete python3-nss 1.0.1^20210803hg9de14a6f77e2-13
%obsolete python3-nuheat 1.0.1-5
%obsolete python3-octave-kernel 0.36.0-4
%obsolete python3-odcs-client 0.9.0-2
%obsolete python3-odcs-common 0.9.0-2
%obsolete python3-odml 1.5.4-7
%obsolete python3-omemo-backend-signal 0.3.1~beta-11
%obsolete python3-onigurumacffi 1.3.0-3
%obsolete python3-openctm 0.0.6-3
%obsolete python3-opendata-transport 0.5.0-3
%obsolete python3-opensensemap-api 0.1.5-24
%obsolete python3-opentelemetry-api 1.27.0-2
%obsolete python3-opentelemetry-contrib-instrumentations 2:0.48~b0-2
%obsolete python3-opentelemetry-distro 2:0.48~b0-2
%obsolete python3-opentelemetry-distro+otlp 2:0.48~b0-2
%obsolete python3-opentelemetry-exporter-opencensus 0.48~b0-2
%obsolete python3-opentelemetry-exporter-otlp 1.27.0-2
%obsolete python3-opentelemetry-exporter-otlp-proto-common 1.27.0-2
%obsolete python3-opentelemetry-exporter-otlp-proto-grpc 1.27.0-2
%obsolete python3-opentelemetry-exporter-otlp-proto-http 1.27.0-2
%obsolete python3-opentelemetry-exporter-prometheus 0.48~b0-2
%obsolete python3-opentelemetry-exporter-richconsole 2:0.48~b0-2
%obsolete python3-opentelemetry-exporter-zipkin 1.27.0-2
%obsolete python3-opentelemetry-exporter-zipkin-json 1.27.0-2
%obsolete python3-opentelemetry-exporter-zipkin-proto-http 1.27.0-2
%obsolete python3-opentelemetry-instrumentation 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-aiohttp-client 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-aiohttp-client+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-aiohttp-server 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-aiohttp-server+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-aiopg 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-aiopg+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-asgi 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-asgi+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-asyncio 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-asyncio+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-asyncpg 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-asyncpg+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-aws-lambda 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-aws-lambda+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-boto 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-boto+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-boto3sqs 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-boto3sqs+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-botocore 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-botocore+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-celery 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-celery+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-dbapi 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-dbapi+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-django 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-django+asgi 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-django+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-elasticsearch 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-elasticsearch+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-fastapi 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-fastapi+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-flask 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-flask+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-httpx 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-httpx+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-jinja2 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-jinja2+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-kafka-python 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-kafka-python+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-logging 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-logging+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-mysql 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-mysql+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-mysqlclient 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-mysqlclient+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-pika 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-pika+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-psycopg 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-psycopg+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-psycopg2 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-psycopg2+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-pymemcache 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-pymemcache+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-pymongo 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-pymongo+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-pymysql 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-pymysql+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-pyramid 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-pyramid+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-redis 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-redis+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-requests 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-requests+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-sqlalchemy 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-sqlalchemy+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-sqlite3 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-sqlite3+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-system-metrics 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-system-metrics+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-threading 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-threading+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-tornado 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-tornado+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-urllib 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-urllib+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-urllib3 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-urllib3+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-wsgi 2:0.48~b0-2
%obsolete python3-opentelemetry-instrumentation-wsgi+instruments 2:0.48~b0-2
%obsolete python3-opentelemetry-opentracing-shim 0.48~b0-2
%obsolete python3-opentelemetry-processor-baggage 2:0.48~b0-2
%obsolete python3-opentelemetry-propagator-aws-xray 1.0.2-2
%obsolete python3-opentelemetry-propagator-b3 1.27.0-2
%obsolete python3-opentelemetry-propagator-jaeger 1.27.0-2
%obsolete python3-opentelemetry-propagator-ot-trace 2:0.48~b0-2
%obsolete python3-opentelemetry-proto 1.27.0-2
%obsolete python3-opentelemetry-resource-detector-azure 0.1.5-5
%obsolete python3-opentelemetry-sdk 1.27.0-2
%obsolete python3-opentelemetry-sdk-extension-aws 2.0.2-2
%obsolete python3-opentelemetry-semantic-conventions 0.48~b0-2
%obsolete python3-opentelemetry-test-utils 0.48~b0-2
%obsolete python3-opentelemetry-util-http 2:0.48~b0-2
%obsolete python3-opentracing 2.4.0-15
%obsolete python3-os-testr 3.0.0-11
%obsolete python3-oscrypto 1.3.0-8
%obsolete python3-oslo-middleware 6.0.0-5
%obsolete python3-oslo-middleware-tests 6.0.0-5
%obsolete python3-ouimeaux 0.8.2-26
%obsolete python3-outdated 0.2.0-18
%obsolete python3-papermill 2.6.0-7
%obsolete python3-papermill+all 2.6.0-7
%obsolete python3-papermill+azure 2.6.0-7
%obsolete python3-papermill+black 2.6.0-7
%obsolete python3-papermill+gcs 2.6.0-7
%obsolete python3-papermill+github 2.6.0-7
%obsolete python3-papermill+hdfs 2.6.0-7
%obsolete python3-papermill+s3 2.6.0-7
%obsolete python3-pastel 0.2.0-18
%obsolete python3-pdc-client 1.8.0-36
%obsolete python3-pep440 0.1.2-9
%obsolete python3-pifpaf 2.2.2-25
%obsolete python3-pingouin 0.5.5-3
%obsolete python3-pint+dask 0.24.4-3
%obsolete python3-pint+xarray 0.24.4-3
%obsolete python3-pkginfo2 30.0.0-7
%obsolete python3-plac 1.4.5-5
%obsolete python3-plaintable 0.1.2-5
%obsolete python3-plotly 5.24.1-5
%obsolete python3-plotnine 0.14.5-3
%obsolete python3-plotnine+extra 0.14.5-3
%obsolete python3-pluggy1.3 1.3.0-10
%obsolete python3-plugnplay 0.5.4-19
%obsolete python3-plumbum 1.7.2-12
%obsolete python3-policyuniverse 1.3.2.20201012-17
%obsolete python3-postgresql 1.2.2-18
%obsolete python3-poyo 0.5.0-19
%obsolete python3-praw 7.8.1-3
%obsolete python3-prawcore 2.4.0-3
%obsolete python3-prewikka 5.2.0-19
%obsolete python3-prewikka-updatedb 5.2.0-17
%obsolete python3-probeinterface 0.2.28-2
%obsolete python3-promise 2.3.0-22
%obsolete python3-psycogreen 1.0.2-17
%obsolete python3-psycopg2-debug 2.9.9-9
%obsolete python3-pvc 0.3.0-27
%obsolete python3-pwncat 0.1.0-18
%obsolete python3-py-algorand-sdk 2.8.0-2
%obsolete python3-py27hash 1.1.0-19
%obsolete python3-py2pack 0.6.3-33
%obsolete python3-pyABF 2.3.8-9
%obsolete python3-pyDes 2.0.1^20240820gite988a5f-3
%obsolete python3-pyactivetwo 0.1-32
%obsolete python3-pyairnow 1.1.0-16
%obsolete python3-pyairvisual 2023.12.0-3
%obsolete python3-pyarlo 0.2.4-17
%obsolete python3-pybalboa 0.10-17
%obsolete python3-pybids 0.19.0-2
%obsolete python3-pybids+plotting 0.19.0-2
%obsolete python3-pybids+test 0.19.0-2
%obsolete python3-pybids+tests 0.19.0-2
%obsolete python3-pybv 0.7.6-6
%obsolete python3-pybv+export 0.7.5-10
%obsolete python3-pycatch22 0.4.4-11
%obsolete python3-pycoingecko 1.3.0-16
%obsolete python3-pycomfoair 0.0.4-16
%obsolete python3-pycomm3 0.10.2-16
%obsolete python3-pydantic-extra-types+all 2.10.5-2
%obsolete python3-pydotplus 2.0.2-34
%obsolete python3-pyeclib 1.6.0-19
%obsolete python3-pyemby 1.6-16
%obsolete python3-pyemd 1.0.0-8
%obsolete python3-pyfim 6.28-20
%obsolete python3-pygatt 5.0.0-3
%obsolete python3-pygeoip 0.2.6-41
%obsolete python3-pygrocy 0.23.0-16
%obsolete python3-pyhomematic 0.1.78-5
%obsolete python3-pyi2cflash 0.2.2-18
%obsolete python3-pyinels 0.5.5-16
%obsolete python3-pyiqvia 2023.12.0-3
%obsolete python3-pykdl 1.5.1-13
%obsolete python3-pylatex 1.4.2-5
%obsolete python3-pylotoncycle 0.2.2-17
%obsolete python3-pymata-express 1.21-14
%obsolete python3-pymochad 0.2.0-17
%obsolete python3-pymod2pkg 0.17.1-24
%obsolete python3-pynamodb 6.1.0-2
%obsolete python3-pynamodb+signals 6.1.0-2
%obsolete python3-pynn 0.12.4-3
%obsolete python3-pynuvo 0.2-16
%obsolete python3-pyopenuv 2.0.0-16
%obsolete python3-pyotgw 1.0b1-17
%obsolete python3-pypcapkit 0.15.5-14
%obsolete python3-pypck 0.7.9-16
%obsolete python3-pypet 0.6.1-9
%obsolete python3-pyphi 1.2.1-27
%obsolete python3-pyprocdev 0.2-32
%obsolete python3-pyriemann 0.8-2
%obsolete python3-pysaml2 7.4.2-6
%obsolete python3-pyserial-asyncio 0.6-14
%obsolete python3-pysignals 0.1.4-6
%obsolete python3-pysmb 1.2.10-3
%obsolete python3-pysmt 0.9.5-10
%obsolete python3-pysqueezebox 0.5.5-18
%obsolete python3-pytapo 0.11-16
%obsolete python3-pytest-error-for-skips 2.0.2-16
%obsolete python3-pytest-ordering 0.6-19
%obsolete python3-pytest-twisted 1.14.3-2
%obsolete python3-pytest7 7.4.3-5
%obsolete python3-pytile 2022.02.0-12
%obsolete python3-pytimeparse 1.1.8-24
%obsolete python3-pytz-deprecation-shim 0.1.0.post0-13
%obsolete python3-pyunicorn 0.8.2-4
%obsolete python3-pyupgrade 3.3.0-10
%obsolete python3-pyvit 0.2.1-24
%obsolete python3-pywatchman 2021.05.10.00-29
%obsolete python3-pyxdf 1.17.0-2
%obsolete python3-pyxdf-examples 1.17.0-2
%obsolete python3-pyxid 1.1-0.33
%obsolete python3-q 2.6-34
%obsolete python3-rabbitvcs 0.19-8
%obsolete python3-rak811 0.7.3-17
%obsolete python3-random2 1.0.2-5
%obsolete python3-rangeparser 0.1.3-18
%obsolete python3-ratinabox 1.15.3-2
%obsolete python3-rawkit 0.6.0-22
%obsolete python3-read-roi 1.6.0-13
%obsolete python3-readlike 0.1.3-16
%obsolete python3-receptor-python-worker 1.4.8-3
%obsolete python3-recordclass 0.22.0.2-4
%obsolete python3-regenmaschine 2022.9.2-10
%obsolete python3-registry 1.4-17
%obsolete python3-remoto 1.2.1-12
%obsolete python3-reparser 1.4.3-16
%obsolete python3-requests-credssp 2.0.0-11
%obsolete python3-restview 3.0.0-11
%obsolete python3-retrying 1.3.3-17
%obsolete python3-ring-doorbell 0.7.1-15
%obsolete python3-rows 0.4.1-25
%obsolete python3-rtmidi 1.5.8-4
%obsolete python3-sarif-om 1.0.4-21
%obsolete python3-scanless 2.2.1-3
%obsolete python3-scikit-build 0.18.1-3
%obsolete python3-scikit-misc 0.5.1-7
%obsolete python3-sciunit 0.2.8-9
%obsolete python3-scripttester 0.1-24
%obsolete python3-sentry-sdk+opentelemetry 2.17.0-4
%obsolete python3-sentry-sdk+opentelemetry-experimental 2.17.0-4
%obsolete python3-serpy 0.3.1-23
%obsolete python3-setuptools_git 1.2-17
%obsolete python3-shade 1.33.0-17
%obsolete python3-shelly 0.2.6-16
%obsolete python3-shodan 1.31.0-5
%obsolete python3-signon 2.1-25
%obsolete python3-simframe 1.0.5-6
%obsolete python3-simplebayes 1.5.8-28
%obsolete python3-simplegeneric 0.8.1-38
%obsolete python3-simplevisor 1.3-13
%obsolete python3-singledispatch 3.4.0.3-35
%obsolete python3-sipvicious 0.3.3-15
%obsolete python3-sklearn-genetic-opt 0.11.1-13
%obsolete python3-sklearn-genetic-opt+seaborn 0.11.1-13
%obsolete python3-slacker 0.14.0-20
%obsolete python3-smi 1.5.0-3
%obsolete python3-snakemake-executor-plugin-azure-batch 0.3.0-4
%obsolete python3-snallygaster 0.0.13-3
%obsolete python3-snuggs 1.4.7-21
%obsolete python3-socialscan 2.0.1-3
%obsolete python3-socks5line 0.0.4-18
%obsolete python3-sortedcollections 2.1.0-19
%obsolete python3-spec 1.4.1-19
%obsolete python3-sphinx-documatt-theme 0.0.6-7
%obsolete python3-sphinx-sitemap 2.6.0-7
%obsolete python3-sphinxcontrib-asyncio 0.3.0-15
%obsolete python3-sphinxcontrib-blockdiag 2.0.0-17
%obsolete python3-sphinxcontrib-github-alt 1.2-19
%obsolete python3-sphinxcontrib-phpdomain 0.12.0-3
%obsolete python3-sphinxcontrib-seqdiag 2.0.0-15
%obsolete python3-sphobjinv 2.3.1.1-3
%obsolete python3-sqlalchemy+mypy 2.0.35-2
%obsolete python3-sqlalchemy+mysql_connector 2.0.43-2
%obsolete python3-sqlmodel 0.0.24-2
%obsolete python3-sqlmodel-slim 0.0.24-2
%obsolete python3-ssdp 1.3.0-7
%obsolete python3-sseclient 0.0.27-17
%obsolete python3-sseclient-py 1.7-17
%obsolete python3-sshpubkeys 3.3.1-28
%obsolete python3-stackprinter 0.2.10-5
%obsolete python3-statsd 3.2.1-33
%obsolete python3-stdiomask 0.0.6-17
%obsolete python3-steam 1.4.4-8
%obsolete python3-stochastic 0.7.0-10
%obsolete python3-stomper 0.4.3-23
%obsolete python3-stopit 1.1.2-14
%obsolete python3-subarulink 0.3.11-17
%obsolete python3-taskflow 5.9.1-4
%obsolete python3-tasmotadevicecontroller 0.0.8-17
%obsolete python3-tbtrim 0.3.1-19
%obsolete python3-tensile 6.2.0-2
%obsolete python3-teslajsonpy 0.11.0-16
%obsolete python3-testing.common.database 2.0.3-19
%obsolete python3-testing.postgresql 1.3.0-24
%obsolete python3-textparser 0.24.0-3
%obsolete python3-textwrap3 0.9.2-18
%obsolete python3-toml 0.10.2-22
%obsolete python3-toposort 1.10-14
%obsolete python3-tosca-parser 2.12.0-3
%obsolete python3-tree-format 0.1.2-25
%obsolete python3-typedecorator 0.0.5-17
%obsolete python3-typish 1.9.3-14
%obsolete python3-ufl 2019.1.0-25
%obsolete python3-universal-pathlib 0.2.5-3
%obsolete python3-upnpy 1.1.8-16
%obsolete python3-urlbuster 0.5.1-6
%obsolete python3-uvloop 0.19.0-6
%obsolete python3-vconnector 0.6.0-19
%obsolete python3-velbus 2.1.2-15
%obsolete python3-vevents 0.1.0-0.21
%obsolete python3-vici 5.9.14-6
%obsolete python3-volkszaehler 0.2.1-16
%obsolete python3-voluptuous-serialize 2.4.0-17
%obsolete python3-vpoller 0.7.3-27
%obsolete python3-vsure 1.6.0-16
%obsolete python3-waqiasync 1.0.0-16
%obsolete python3-watchgod 0.8.2-11
%obsolete python3-waterfurnace 1.1.0-17
%obsolete python3-webthing 0.15.0-17
%obsolete python3-webthing-ws 0.1.0-20
%obsolete python3-whichcraft 0.6.1-17
%obsolete python3-wiffi 1.0.1-16
%obsolete python3-winacl 0.1.9-3
%obsolete python3-winsspi 0.0.11-3
%obsolete python3-wled 0.4.4-17
%obsolete python3-wloc 1.1.0-9
%obsolete python3-ws4py 0.5.1-19
%obsolete python3-wsgi_intercept 1.12.0-8
%obsolete python3-xboxapi 2.0.1-16
%obsolete python3-xiaomi-gateway 0.13.3-16
%obsolete python3-xpath-expressions 1.0.2-18
%obsolete python3-xunitparser 1.3.4-11
%obsolete python3-yappi 1.6.0-4
%obsolete python3-yaswfp 0.9.3-21
%obsolete python3-yattag 1.16.0-3
%obsolete python3-zake 0.2.2-35
%obsolete python3-zc-customdoctests 1.0.1-42
%obsolete python3-zdaemon 4.2.0-30
%obsolete python3-zm 0.5.2-17
%obsolete rabbitvcs-caja 0.19-8
%obsolete rabbitvcs-cli 0.19-8
%obsolete rabbitvcs-nautilus 0.19-8
%obsolete rabbitvcs-nemo 0.19-8
%obsolete rapid-photo-downloader 0.9.33-15
%obsolete receptor 1.4.8-3
%obsolete receptorctl 1.4.8-3
%obsolete restview 3.0.0-11
%obsolete retext 8.0.0-10
%obsolete rows 0.4.1-25
%obsolete rst2txt 1.1.0-26
%obsolete scanless 2.2.1-3
%obsolete secrets 9.6-4
%obsolete sgtk-menu 1.4.1-17
%obsolete shodan 1.31.0-5
%obsolete sipvicious 0.3.3-15
%obsolete snallygaster 0.0.13-3
%obsolete socialscan 2.0.1-3
%obsolete standard-test-roles 4.13-2
%obsolete standard-test-roles-inventory-qemu 4.13-2
%obsolete sysmontask 1.3.9-17
%obsolete trace-summary 0.92-12
%obsolete urlbuster 0.5.1-6
%obsolete vpoller 0.7.3-27
%obsolete wad 0.4.6-18
%obsolete wapiti 3.0.2-20
%obsolete webtech 1.2.11-13
%obsolete wfuzz 3.1.0-17
%obsolete wxGlade 1.1.1-2
%obsolete x-tile 3.3-17
%obsolete xortool 1.0.2-3
# Packages which weren't successfully built with Python 3.14
# and weren't retired (bugzilla in ASSIGNED state)
%obsolete cjdns-graph 21.1-17
%obsolete conda-build 24.11.2-3
%obsolete howdoi 2.0.20-12
%obsolete psi4 1:1.9.1-7
%obsolete python3-cjdns 21.1-17
%obsolete python3-conda-build 24.11.2-3
%obsolete python3-dataclassy 1.0.1-4
%obsolete python3-dolfin 2019.1.0.post0-58
%obsolete python3-ffc 2019.1.0.post0-25
%obsolete python3-optking 0.3.0-7
%obsolete python3-pamela 1.2.0-3
%obsolete python3-qcengine 0.30.0-5
%obsolete zeekctl 6.0.4-2
%obsolete zeek-zkg 6.0.4-2


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
