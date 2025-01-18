# Disable in source builds on EPEL <9
%undefine __cmake_in_source_build
%undefine __cmake3_in_source_build

%define csexec_archs aarch64 ppc64le s390x x86_64

Name:       cswrap
Version:    2.2.4
Release:    3%{?dist}
Summary:    Generic compiler wrapper

License:    GPL-3.0-or-later
URL:        https://github.com/csutils/%{name}
Source0:    https://github.com/csutils/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz
Source1:    https://github.com/csutils/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz.asc

# gpg --keyserver pgp.mit.edu --recv-key 992A96E075056E79CD8214F9873DB37572A37B36
# gpg --output kdudka.pgp --armor --export kdudka@redhat.com
Source2:    kdudka.pgp

BuildRequires: asciidoc
BuildRequires: cmake3
BuildRequires: gcc
BuildRequires: gnupg2

# csmock copies the resulting cswrap binary into mock chroot, which may contain
# an older (e.g. RHEL-7) version of glibc, and it would not dynamically link
# against the old version of glibc if it was built against a newer one.
# Therefore, we link glibc statically.
BuildRequires: glibc-static

# The test-suite runs automatically trough valgrind if valgrind is available
# on the system.  By not installing valgrind into mock's chroot, we disable
# this feature for production builds on architectures where valgrind is known
# to be less reliable, in order to avoid unnecessary build failures (see RHBZ
# #810992, #816175, and #886891).  Nevertheless developers are free to install
# valgrind manually to improve test coverage on any architecture.
%ifarch %{ix86} x86_64
BuildRequires: valgrind
%endif

%description
Generic compiler wrapper used by csmock to capture diagnostic messages.

# csexec is available on architectures defined in %%{csexec_archs} only
%ifarch %{csexec_archs}
%package -n csexec
Summary: Dynamic linker wrapper
Conflicts: csexec < %{version}-%{release}

%description -n csexec
This package contains csexec - a dynamic linker wrapper.  The wrapper can
be used to run dynamic analyzers and formal verifiers on source RPM package
fully automatically.
%endif

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake3 \
    -DPATH_TO_WRAP=\"%{_libdir}/cswrap\" \
    -DSTATIC_LINKING=ON
%cmake3_build

%check
%ctest3

%install
%cmake3_install

install -m0755 -d "%{buildroot}%{_libdir}"{,/cswrap}
for i in c++ cc g++ gcc clang clang++ cppcheck smatch \
    divc++ divcc diosc++ dioscc gclang++ gclang goto-gcc \
    %{_arch}-redhat-linux-c++ \
    %{_arch}-redhat-linux-g++ \
    %{_arch}-redhat-linux-gcc
do
    ln -s ../../bin/cswrap "%{buildroot}%{_libdir}/cswrap/$i"
done

%files
%license COPYING
%doc README
%{_bindir}/cswrap
%{_libdir}/cswrap
%{_mandir}/man1/%{name}.1*

%ifarch %{csexec_archs}
%files -n csexec
%license COPYING
%{_bindir}/csexec
%{_bindir}/csexec-loader
%{_libdir}/libcsexec-preload.so
%{_mandir}/man1/csexec.1*
%endif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 25 2024 Kamil Dudka <kdudka@redhat.com> 2.2.4-1
- update to latest upstream

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 06 2023 Kamil Dudka <kdudka@redhat.com> 2.2.3-1
- migrate to SPDX license
- update to latest upstream

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 06 2022 Kamil Dudka <kdudka@redhat.com> 2.2.2-1
- update to latest upstream

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Kamil Dudka <kdudka@redhat.com> 2.2.1-1
- update to latest upstream

* Wed Mar 23 2022 Kamil Dudka <kdudka@redhat.com> 2.2.0-1
- update to latest upstream

* Tue Mar 15 2022 Kamil Dudka <kdudka@redhat.com> 2.1.0-3
- verify GPG signature of upstream tarball when building the package

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 03 2021 Kamil Dudka <kdudka@redhat.com> 2.1.0-1
- update to latest upstream

* Tue Aug 31 2021 Kamil Dudka <kdudka@redhat.com> 2.0.1-1
- update to latest upstream

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Kamil Dudka <kdudka@redhat.com> 1.9.2-1
- update to latest upstream

* Wed Feb 17 2021 Kamil Dudka <kdudka@redhat.com> 1.9.1-1
- update to latest upstream

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 20 2020 Kamil Dudka <kdudka@redhat.com> 1.9.0-1
- update to latest upstream

* Wed Aug 19 2020 Kamil Dudka <kdudka@redhat.com> 1.8.0-1
- update to latest upstream

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 Kamil Dudka <kdudka@redhat.com> 1.6.0-1
- update to latest upstream

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Kamil Dudka <kdudka@redhat.com> 1.5.0-1
- update to latest upstream

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Kamil Dudka <kdudka@redhat.com> 1.4.0-3
- add explicit BR for the gcc compiler

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Kamil Dudka <kdudka@redhat.com> 1.4.0-1
- update to latest upstream

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Kamil Dudka <kdudka@redhat.com> 1.3.4-5
- fix intermittent test-suite failures on slow Koji build hosts

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Kamil Dudka <kdudka@redhat.com> 1.3.4-3
- fix intermittent test-suite failures on slow Koji build hosts

* Thu Jul 20 2017 Kamil Dudka <kdudka@redhat.com> 1.3.4-2
- cswrap.1: replace a reference to fedorahosted.org

* Wed Feb 15 2017 Kamil Dudka <kdudka@redhat.com> 1.3.4-1
- update to latest upstream release
- update project URL and source URL

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Kamil Dudka <kdudka@redhat.com> 1.3.3-1
- update to latest upstream

* Mon Mar 21 2016 Kamil Dudka <kdudka@redhat.com> 1.3.2-1
- update to latest upstream

* Wed Feb 03 2016 Kamil Dudka <kdudka@redhat.com> 1.3.1-1
- update to latest upstream

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 18 2015 Kamil Dudka <kdudka@redhat.com> 1.3.0-1
- update to latest upstream

* Mon Jan 19 2015 Kamil Dudka <kdudka@redhat.com> 1.2.1-1
- update to latest upstream

* Thu Nov 06 2014 Kamil Dudka <kdudka@redhat.com> 1.2.0-1
- update to latest upstream

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Kamil Dudka <kdudka@redhat.com> 1.0.5-1
- update to latest upstream

* Thu Jul 17 2014 Kamil Dudka <kdudka@redhat.com> 1.0.4-1
- update to latest upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 27 2014 Kamil Dudka <kdudka@redhat.com> 1.0.3-1
- update to latest upstream

* Mon Mar 10 2014 Kamil Dudka <kdudka@redhat.com> 1.0.2-2
- abandon RHEL-5 compatibility (#1066028)

* Wed Feb 19 2014 Kamil Dudka <kdudka@redhat.com> 1.0.2-1
- packaged for Fedora
