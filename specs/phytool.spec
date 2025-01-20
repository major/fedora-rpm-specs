Name:           phytool
Version:        2
Release:        5%{?dist}
Summary:        CLI for Linux MDIO register access

License:        GPL-2.0-or-later
URL:            https://github.com/wkz/phytool/
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz

## Patches go here.
## https://github.com/wkz/phytool/pull/14
Patch0:         0001-Checked-return-of-asprintf-for-lack-of-memory-and-er.patch
## https://github.com/wkz/phytool/pull/15
# Fix Makefile to create PREFIXdir
# Fix Makefile to use sha512sum instead of md5sum for FIPS systems
Patch1:         0002-Make-fixes-to-Makefile-found-in-Fedora-spec-file-rev.patch
## https://github.com/wkz/phytool/pull/16
# Fix Makefile to create manpage
# Add man pages written by Ben Beasley
Patch2:         0003-Add-man-pages-and-adjust-Makefile-for-man-pages.patch

BuildRequires:  make
BuildRequires:  gcc


%description
phytool is a command line tool for reading MDIO registers and working
with Marvell Link register access

%prep
%autosetup

%build
%set_build_flags
%make_build

%install
%make_install PREFIX='%{_prefix}'

%files
%license LICENSE
%doc README.md
%{_bindir}/phytool
%{_bindir}/mv6tool
%{_mandir}/man8/phytool.8*
%{_mandir}/man8/mv6tool.8*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Stephen Smoogen <smooge@fedoraproject.org> - 2-3
- Update comments to point to upstream PR
- Update man page.
- Fixed man page entry to match spec review

* Wed Jan 17 2024 Stephen Smoogen <smooge@fedoraproject.org> - 2-2
- Make changes to match spec review https://bugzilla.redhat.com/show_bug.cgi?id=2258110
- Make debugsource not run on el9
- Fix phytool code for asprintf warning
- Fix makefile for missing bindir and md5sum

* Thu Jan 11 2024 Stephen Smoogen <ssmoogen@redhat.com> 2-1
- Initial spec file creation.
- Confirm license in SPDX format
