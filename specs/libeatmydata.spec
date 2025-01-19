Name:           libeatmydata
Version:        130
Release:        13%{?dist}
Group:          Development/Tools
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
Summary:        Library and utilities designed to disable fsync and friends
BuildRequires:  gcc, make, libtool, strace, gnupg
Source0:        https://www.flamingspork.com/projects/libeatmydata/%{name}-%{version}.tar.gz
Source1:        https://www.flamingspork.com/projects/libeatmydata/%{name}-%{version}.tar.gz.asc
Source2:        https://flamingspork.com/stewart.gpg
# Man page to be included upstream soon...
Source3:        https://salsa.debian.org/debian/libeatmydata/-/raw/048c4ea3/debian/eatmydata.1
Patch0:         libeatmydata-sync-file-range.patch

URL:            https://www.flamingspork.com/projects/libeatmydata/
%if !(0%{?rhel} && 0%{?rhel} < 8)
Recommends: eatmydata
%endif

%description
This package contains a small LD_PRELOAD library (libeatmydata) and a couple 
of helper utilities (eatmydata) designed to transparently disable fsync and
friends (like open(O_SYNC)). This has two side-effects: making software that
writes data safely to disk a lot quicker and making this software no longer 
crash safe.

%package -n eatmydata
Summary: Utility to disable fsync() and friends for the command specified 
# Explict requires as the main package is a shell script that does an LD_PRELOAD
# and thus we don't get automatic dependencies!
Requires: %{name}

%description -n eatmydata
The eatmydata script does the heavy lifting of LD_PRELOAD for the command
specified. You can also symlink a command to the eatmydata wrapper and the
wrapper will find the command in PATH and then execute it after setting up
the libeatmydata LD_PRELOAD

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%configure --enable-static=no
%make_build

%install

%make_install
mkdir -p %{buildroot}%{_mandir}/man1/
install -m444 -p %{SOURCE3} %{buildroot}%{_mandir}/man1/

%if !0%{?fedora} || 0%{?fedora} < 36
find %{buildroot} -name "*.la" -type f -delete
%endif

%check
%{__make} check

%files -n eatmydata
%{_bindir}/eatmydata
%{_libexecdir}/eatmydata.sh
%{_mandir}/man1/eatmydata.1*
%doc README.md AUTHORS
%license COPYING

%files
%{_libdir}/*.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 130-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 130-12
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 130-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 130-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 130-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 130-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 130-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Peter Fordham <peter.fordham@gmail.com> - 130-6
- Include sync_file_range header for C99 compatibility.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 130-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 11 2022 Stewart Smith <stewart@flamingspork.com> - 130-4
- Fix Summary
- Build eatmydata per-arch as script contains arch specific dirs
  See https://bugzilla.redhat.com/show_bug.cgi?id=2099313
* Tue May 31 2022 Stewart Smith <stewart@flamingspork.com> - 130-3
- Fixes for submitting packaging to Fedora
* Fri May 27 2022 Stewart Smith <stewart@flamingspork.com> - 130-2
- Package for Fedora
* Sun Oct 10 2021 Stewart Smith <stewart@flamingspork.com> - 130-1
- version 130, add syncfs() wrapper
* Sat Apr 10 2021 Stewart Smith <stewart@flamingspork.com> - 129-1
- Version 129, as always, bug fix release
* Fri Jul 26 2013 Jaroslav Kortus <jkortus@redhat.com> - 82-1
- Version 82, bug fix release
- spec file changed to meet fedora packaging guidelines
* Fri May 18 2013 Stewart Smith <stewart@flamingspork.com> - 79
- Version 79, bug fix release
* Fri Mar 08 2013 Alexey Bychko <alexey.bychko@percona.com> - 0.1
- Version 0.1, initial package for RPM-based systems


