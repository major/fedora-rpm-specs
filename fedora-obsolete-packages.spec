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
Version:    40
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
# Remove in F42
# %%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=1234567
# %%obsolete foo 3.5-7

# Remove in F41
# TeXLive sometimes just kills off components without notice, so there is no ticket.
# These items were removed with TeXLive 2023 (first in Fedora 39) and have no replacement.
%obsolete_ticket Ishouldfileaticket
%obsolete texlive-elegantbook svn64122-67
%obsolete texlive-elegantnote svn62989-67
%obsolete texlive-elegantpaper svn62989-67
%obsolete texlive-tablestyles svn34495.0-67
%obsolete texlive-tablestyles-doc svn34495.0-67
%obsolete texlive-pgf-cmykshadings svn52635-67

# Remove in F41
%obsolete_ticket https://src.fedoraproject.org/rpms/jython/c/5b613bd06ba08cea22e9906646b3a37aca4280c1?branch=rawhide
%obsolete jython 2.7.1-17

# Remove in F41
%obsolete_ticket https://src.fedoraproject.org/rpms/libgweather/c/6cd1eaa540e6acb1b1c26009dd5fac3d481de086?branch=rawhide
%obsolete libgweather 40.0-7
%obsolete libgweather-devel 40.0-7

# Remove in F41
%obsolete_ticket https://src.fedoraproject.org/rpms/sssd/c/cf3c8f20eeb0e7fe8cc2cfb0d02db9e5f9ddf04e?branch=rawhide
%obsolete sssd-libwbclient 2.3.1-3
%obsolete sssd-libwbclient-devel 2.3.1-3

# Remove in F41
# Removed packages with broken dependencies on Python 3.11
%obsolete_ticket https://bugzilla.redhat.com/show_bug.cgi?id=2233409
%obsolete 5minute 0.2.32-14
%obsolete androguard 3.3.5-13
%obsolete awake 1.0-31
%obsolete datagrepper 1.0.1-3
%obsolete datanommer-commands 1.0.3-5
%obsolete drat-tools 1.0.3-16
%obsolete gdeploy 3.0.0-15
%obsolete gnome-activity-journal 1.0.0-8
%obsolete holland 1.2.10-3
%obsolete holland-common 1.2.10-3
%obsolete holland-commvault 1.2.10-3
%obsolete holland-lvm 1.2.10-3
%obsolete holland-mariabackup 1.2.10-3
%obsolete holland-mongodump 1.2.10-3
%obsolete holland-mysql 1.2.10-3
%obsolete holland-mysqldump 1.2.10-3
%obsolete holland-mysqllvm 1.2.10-3
%obsolete holland-pg_basebackup 1.2.10-3
%obsolete holland-pgdump 1.2.10-3
%obsolete holland-xtrabackup 1.2.10-3
%obsolete imgbased 1.2.5-0.2
%obsolete lnst 15-16
%obsolete lnst-ctl 15-16
%obsolete lnst-slave 15-16
%obsolete nodepool 3.13.1-6
%obsolete nodepool-builder 3.13.1-6
%obsolete nodepool-launcher 3.13.1-6
%obsolete openscap-daemon 0.1.10-20
%obsolete pynag 1.1.2-12
%obsolete pynag-examples 1.1.2-12
%obsolete python3-APScheduler 3.8.0-4
%obsolete python3-Pyped 1.4-26
%obsolete python3-aioambient 1.3.0-6
%obsolete python3-aiocurrencylayer 1.0.4-3
%obsolete python3-aioguardian 1.0.4-9
%obsolete python3-awake 1.0-31
%obsolete python3-bintrees 2.0.1-31
%obsolete python3-certbot-dns-cloudxns 1.32.0-2
%obsolete python3-clikit 0.6.2-8
%obsolete python3-cmdln 2.0.0-25
%obsolete python3-colour-runner 0.0.4-28
%obsolete python3-coreapi 2.3.3-10
%obsolete python3-coreschema 0.0.4-10
%obsolete python3-cornice-sphinx 1:0.3-21
%obsolete python3-cotyledon-tests 1.7.3-15
%obsolete python3-cypy 0.2.0-13
%obsolete python3-datanommer-consumer 0.8.1-20
%obsolete python3-datanommer-models 1.0.4-5
%obsolete python3-django-contact-form 1.4.2-20
%obsolete python3-django-robots 3.1.0-18
%obsolete python3-django3 3.2.19-2
%obsolete python3-drat 1.0.3-16
%obsolete python3-drf-yasg 1.20.0-8
%obsolete python3-drf-yasg+validation 1.20.0-8
%obsolete python3-editdistance-s 1.0.0-8
%obsolete python3-fbthrift-devel 2022.07.11.00-3
%obsolete python3-flask-restful 0.3.9-7
%obsolete python3-folly-devel 2022.07.11.00-5
%obsolete python3-formats 0.1.1-26
%obsolete python3-frozen-flask 0.12-25
%obsolete python3-google-cloud-bigquery-datatransfer+libcst 3.7.0-2
%obsolete python3-google-cloud-containeranalysis+libcst 2.9.0-2
%obsolete python3-google-cloud-dataproc+libcst 5.0.0-2
%obsolete python3-google-cloud-dlp+libcst 3.8.0-2
%obsolete python3-google-cloud-redis+libcst 2.9.0-3
%obsolete python3-googletrans 4.0.0~rc1-10
%obsolete python3-graphitesend 0.10.0-23
%obsolete python3-grpcio-admin 1.48.4-9
%obsolete python3-grpcio-csds 1.48.4-9
%obsolete python3-gzipstream 2.8.6-18
%obsolete python3-h5py-openmpi 3.7.0-5
%obsolete python3-hs-dbus-signature 0.07-11
%obsolete python3-imgbased 1.2.5-0.2
%obsolete python3-importmagic 0.1.7-24
%obsolete python3-itypes 1.2.0-8
%obsolete python3-jsonmodels 2.4-14
%obsolete python3-jupyter-server-ydoc 0.7.0-2
%obsolete python3-krbcontext 0.10-13
%obsolete python3-lasagne 0.1-26
%obsolete python3-libproxy 0.4.18-7
%obsolete python3-lightblue 0.1.4-18
%obsolete python3-luxcorerender 2.6-22
%obsolete python3-martian 0.15-20
%obsolete python3-networkmanager 2.2-10
%obsolete python3-okaara 1.0.37-23
%obsolete python3-operator-courier 2.1.9-10
%obsolete python3-pacpy 1.0.3.1-17
%obsolete python3-pecan-notario 0.0.3-26
%obsolete python3-phabricator 0.7.0-21
%obsolete python3-pyPEG2 2.15.2-25
%obsolete python3-pydenticon 0.3.1-19
%obsolete python3-pygpu 0.7.6-20
%obsolete python3-pygpu-devel 0.7.6-20
%obsolete python3-pyngus 2.3.0-15
%obsolete python3-pynlpl 1.2.7-15
%obsolete python3-pyoptical 0.4-26
%obsolete python3-pytelegrambotapi 4.11.0-2
%obsolete python3-pytest-beakerlib 0.7.1-21
%obsolete python3-pytest-capturelog 0.7-28
%obsolete python3-pytest-flake8 1.1.1-5
%obsolete python3-pytest-sanic 1.9.1-4
%obsolete python3-pytest-toolbox 0.4-13
%obsolete python3-qrencode 1.2~git.1.b75219e-16
%obsolete python3-restsh 0.2-23
%obsolete python3-signalfd 0.1-34
%obsolete python3-simplemediawiki 1.2.0-0.32
%obsolete python3-simpy 3.0.9-24
%obsolete python3-slip 0.6.4-30
%obsolete python3-slip-dbus 0.6.4-30
%obsolete python3-spdx 2.5.0-11
%obsolete python3-spdx-lookup 0.3.2-11
%obsolete python3-theano 1.1.2-7
%obsolete python3-tortilla 0.4.1-26
%obsolete python3-upt-cpan 0.5-12
%obsolete python3-upt-fedora 0.3-11
%obsolete python3-upt-pypi 0.4-11
%obsolete python3-upt-rubygems 0.2-11
%obsolete python3-versiontools 1.9.1-34
%obsolete python3-vertica 1.0.5-5
%obsolete python3-visionegg-quest 1.1-17
%obsolete python3-xds-protos 0.0.11-31
%obsolete python3-xtermcolor 1.3-28
%obsolete python3-zabbix-api-erigones 1.2.4-20
%obsolete resultsdb 2.2.0-14
%obsolete resultsdb_frontend 2.1.2-14
%obsolete scudcloud 1.65-17
%obsolete sendKindle 3-15
%obsolete sgmanager 2.0.0-14
%obsolete stgit 1.5-5
%obsolete sugar-paint 70-12
%obsolete thunarx-python 0.5.2-7
%obsolete transmageddon 1.5-31
%obsolete upt 0.10.3-14
%obsolete vitables 3.0.2-17
%obsolete vitables-doc 3.0.2-17
%obsolete whipper-plugin-eaclogger 0.5.0-11
%obsolete yokadi 1.2.0-7

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
