# Sadness, this directory is hardcoded everywhere
%global _libdir /usr/lib

# SUSE guys use OBS to automatically handle release numbers,
# when rebasing check what they are using on
# https://download.opensuse.org/repositories/openSUSE:/Tools/Fedora_36/src/
# update the obsrel to match the upstream release number
%global obsrel 398.1

# Actual release
%global baserelease 1

Name:           obs-build
Version:        20220927
Release:        %{obsrel}.%{baserelease}%{?dist}
Summary:        A generic package build script

License:        (GPLv2 or GPLv3) and GPLv2+
URL:            https://github.com/openSUSE/obs-build

# Tarball retrieved from
# https://build.opensuse.org/package/show/openSUSE:Tools/build
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Potentially not upstreamable patches
## Restore shebang to openstack-console script
Patch0501:      0501-Revert-Drop-shebang-line-from-openstack-console.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  python3-devel
BuildRequires:  /usr/bin/prove
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(FindBin)
BuildRequires:  (perl(YAML::PP) or perl(YAML::XS))
BuildRequires:  perl(POSIX)
Requires:       bash, perl-interpreter, binutils, tar
Requires:       gzip, bzip2, xz, zstd
Requires:       python3-websocket-client
Recommends:     perl(Archive::Tar)
Recommends:     /sbin/mkfs.ext3
Recommends:     /usr/bin/qemu-kvm
Recommends:     bsdtar
Recommends:     qemu-linux-user
Recommends:     zstd
Recommends:     perl(Config::IniFiles)
Recommends:     perl(Date::Language)
Recommends:     perl(Date::Parse)
Recommends:     perl(LWP::UserAgent)
Recommends:     perl(Net::SSL)
Recommends:     perl(Pod::Usage)
Recommends:     perl(Time::Zone)
Recommends:     perl(URI)
Recommends:     perl(XML::Parser)
Recommends:     perl(YAML::LibYAML)
Requires:       perl(POSIX)

Provides:       build = %{version}-%{release}
Requires:       %{name}-mkbaselibs = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     %{name}-mkdrpms = %{version}-%{release}
%endif

%description
This package provides a script for building packages in a chroot environment.
It is commonly used with the Open Build Service as the engine for building
packages for a wide variety of distributions.

%package mkbaselibs
Summary:        Tools to generate base library packages
Provides:       build-mkbaselibs = %{version}-%{release}
AutoReq:        no

%description mkbaselibs
This package contains the parts which may be installed in the inner build
system for generating base library packages.

%package mkdrpms
Summary:        Tools to generate DeltaRPMs
Provides:       build-mkdrpms = %{version}-%{release}
Requires:       deltarpm
Requires:       %{name} = %{version}-%{release}

%description mkdrpms
This package contains the parts which may be installed in the inner build
system for generating DeltaRPM packages.

%prep
%autosetup -p1


%build
# Nothing to do here


%install
%make_install
pushd %{buildroot}%{_libdir}/build/configs/
touch default.conf
test -e default.conf
popd

# Install man pages
install -d -m 0755 %{buildroot}%{_mandir}/man1
install -m 0644 build.1* %{buildroot}%{_mandir}/man1/
install -m 0644 buildvc.1* %{buildroot}%{_mandir}/man1/
install -m 0644 unrpm.1* %{buildroot}%{_mandir}/man1/

# Fix Python shebang for openstack-console
sed -e "s|#!/usr/bin/python|#!%{__python3}|" \
    -i %{buildroot}%{_libdir}/build/openstack-console

%check
%make_build test

%files
%license COPYING
%doc README.md
%{_bindir}/build
%{_bindir}/buildvc
%{_bindir}/unrpm
%{_bindir}/pbuild
%{_libdir}/build
%{_mandir}/man1/build.1*
%{_mandir}/man1/buildvc.1*
%{_mandir}/man1/unrpm.1*
%{_mandir}/man1/pbuild.1*
%exclude %{_libdir}/build/mkbaselibs
%exclude %{_libdir}/build/baselibs*
%exclude %{_libdir}/build/mkdrpms

%files mkbaselibs
%{_libdir}/build/mkbaselibs
%{_libdir}/build/baselibs*

%files mkdrpms
%{_libdir}/build/mkdrpms


%changelog
* Tue Sep 27 2022 Dan Čermák <dan.cermak@cgc-instruments.com> - 20220927-398.1.1
- New upstream release 20220927, fixes rhbz#2130176

* Tue Aug 16 2022 Dan Čermák <dan.cermak@cgc-instruments.com> - 20220812-393.9.1
- New upstream release 20220812

* Thu Aug 11 2022 Dan Čermák <dan.cermak@cgc-instruments.com> - 20220620-393.9.1
- New upstream release 20220620

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20211125-376.1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20211125-376.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 26 2021 Dan Čermák <dan.cermak@cgc-instruments.com> - 20211125-376.1.1
- New upstream release 20211125, fixes rhbz#2026807

* Tue Oct 26 2021 Dan Čermák <dan.cermak@cgc-instruments.com> - 20211025-374.2.1
- New upstream release 20211025, fixes rhbz#2017238

* Tue Sep 28 2021 Dan Čermák <dan.cermak@cgc-instruments.com> - 20210902-373.7.1
- New upstream release 20210902

* Tue Aug 31 2021 Dan Čermák <dan.cermak@cgc-instruments.com> - 20210830-372.1.1
- New upstream release 20210830

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20210120-367.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 19 2021 Dan Čermák <dan.cermak@cgc-instruments.com> - 20210120-367.1.1
- New upstream release 20210120
- Fixes rhbz#1787804

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20191205-325.1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20191205-325.1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20191205-325.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 27 2019 Neal Gompa <ngompa13@gmail.com> - 20191205-325.1.1
- Update to new release

* Mon Nov 18 2019 Neal Gompa <ngompa13@gmail.com> - 20191114-323.1.1
- Update to new release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20190321-314.1.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 24 2019 Neal Gompa <ngompa13@gmail.com> - 20190321-314.1.1
- Update to new release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180816-291.1.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Neal Gompa <ngompa13@gmail.com> - 20180816-291.1.1
- Update to new release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171023-267.1.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20171023-267.1.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 05 2017 Neal Gompa <ngompa13@gmail.com> - 20171023-267.1.1
- Update to new release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170317-237.1.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 20170317-237.1.1.1
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Sat Mar 18 2017 Neal Gompa <ngompa13@gmail.com> - 20170317-237.1.1
- Update to new release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20161025-231.1.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 26 2016 Neal Gompa <ngompa13@gmail.com> - 20161025-231.1.1
- Initial import (#1381661)
- Initial packaging based on SUSE and Josef Strzibny's packaging
