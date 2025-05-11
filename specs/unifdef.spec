Name:           unifdef
Version:        2.12
Release:        %autorelease
Summary:        Selectively remove C preprocessor conditionals

# The entire source is BSD-2-Clause, except:
#
# BSD-3-Clause:
#   - unifdef.1
#   - FreeBSD/* (removed in %%prep, not used in the build)
#
# From unifdef.c:
#
#   This code was derived from software contributed to Berkeley by Dave Yost.
#   It was rewritten to support ANSI C by Tony Finch. The original version of
#   unifdef carried the 4-clause BSD copyright licence. None of its code
#   remains in this version (though some of the names remain) so it now carries
#   a more liberal licence.
License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://dotat.at/prog/unifdef/
%global forgeurl https://github.com/fanf2/unifdef
# We package from the manual release archive on the website rather than from
# the automatic GitHub archive,
#   %%{forgeurl}/archive/unifdef-%%{version}/unifdef-unifdef-%%{version}.tar.gz
# even though the latter has advantages for auditability. Building unifdef
# requires version.h and version.sh at the top level, and producing these
# requires git history. For 2.12, the release archive and GitHub archive were
# manually compared, and no unexpected discrepancies were found.
Source:         https://dotat.at/prog/unifdef/unifdef-%{version}.tar.xz

# tests: support both *BSD and Linux ls -l permissions output
# https://github.com/fanf2/unifdef/pull/14
Patch:          %{forgeurl}/pull/14.patch

# Fix fgets(..., size=1)
# https://github.com/fanf2/unifdef/pull/15
#
# Further discussion in https://github.com/fanf2/unifdef/pull/19 and
# https://gcc.gnu.org/PR120205.
Patch:          %{forgeurl}/pull/15.patch

# Don't use C23 constexpr keyword
# https://github.com/fanf2/unifdef/pull/19
# Fixes compatibility with GCC 15, which defaults to C23
Patch:          %{forgeurl}/pull/19.patch

BuildRequires:  gcc
BuildRequires:  make

%description
The unifdef utility selectively processes conditional C preprocessor #if
and #ifdef directives. It removes from a file both the directives and the
additional text that they delimit, while otherwise leaving the file alone.


%prep
%autosetup -p1
# Show that we do not use the sources in FreeBSD – even though this does not
# simplify the License, since unifdef.1 is still BSD-3-Clause.
rm -rv FreeBSD/


%build
%make_build


%install
%make_install prefix='%{_prefix}'


%check
PATH="%{buildroot}%{_bindir}:${PATH}" %make_build test


%files
%license COPYING

# We do not install Changelog as documentation because it is a verbose dump of
# git history, and the result would be larger than the rest of the package
# combined.
%doc README
# Just a nicely text-formatted version of the man page
%doc unifdef.txt

%{_bindir}/unifdef
%{_bindir}/unifdefall

%{_mandir}/man1/unifdef.1*
%{_mandir}/man1/unifdefall.1*


%changelog
%autochangelog
