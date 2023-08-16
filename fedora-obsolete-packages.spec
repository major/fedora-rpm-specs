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
