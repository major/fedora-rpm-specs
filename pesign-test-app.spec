Summary: Simple pesign test target
Name: pesign-test-app
Version: 5
Release: 28%{?dist}
License: GPLv2
URL: https://github.com/vathpela/pesign-test-app
BuildRequires: make
BuildRequires: gcc
BuildRequires: acl
BuildRequires: git
BuildRequires: gnu-efi
BuildRequires: gnu-efi-devel
BuildRequires: pesign >= 0.104-1
BuildRequires: efi-srpm-macros
# ExclusiveArch: i686 x86_64 ia64 aarch64
ExclusiveArch: x86_64

# pesign-test-app generates no binaries that run under the installed OS, so
# debuginfo is useless
%global debug_package %{nil}

%global __pesign_client_token "OpenSC Card (Fedora Signer)"

# there is no tarball at github, of course.  To get this version do:
# git clone https://github.com/vathpela/pesign-test-app.git
# git checkout %%{version}
Source0: pesign-test-app-%{version}.tar.bz2

Patch0001: 0001-Fix-gnu-efi-include-path.patch

%description
This package contains a very simple UEFI application that effectively does
nothing.  The entire purpose of this is to provide a safe app to be signed,
so that we don't have to build large applications in order to test that
deployments of new pesign versions into build infrastructure have succeeded.

%prep
%autosetup -S git

%build
make LIBDIR=%{_libdir} DATADIR=%{_datadir} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_OPT_LDFLAGS"
cp %{name}.efi %{name}-unsigned.efi
id
ls -ld /var/run/pesign || :
getfacl /var/run/pesign || :
ls -l /var/run/pesign/socket || :
getfacl /var/run/pesign/socket || :
ls -ld /run/pesign || :
getfacl /run/pesign || :
ls -l /run/pesign/socket || :
getfacl /run/pesign/socket || :

%define pe_signing_cert grub2-signer
if ! true ; then
	cp %{name}-unsigned.efi bzImage.signed
	%pesign -s -i bzImage.signed -o bzImage.signed -a redhatsecurebootca5.cer -c redhatsecureboot501.cer -n redhatsecureboot501
	%pesign -s -i bzImage.signed -o bzImage.signed -a redhatsecurebootca1.cer -c redhatsecureboot301.cer -n redhatsecureboot301
	mv bzImage.signed %{name}-signed.efi
else
	cp %{name}-unsigned.efi %{name}-unsigned.0.efi
	%pesign -s -i %{name}-unsigned.0.efi -o %{name}.tmp.efi -a redhatsecurebootca5.cer -c redhatsecureboot501.cer -n redhatsecureboot501
	%define pe_signing_cert fwupd-signer
	%pesign -s -i %{name}.tmp.efi -o %{name}-signed.efi -a redhatsecurebootca1.cer -c redhatsecureboot301.cer -n redhatsecureboot301
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}
make LIBDIR=%{_libdir} INSTALLROOT=%{buildroot} DATADIR=%{_datadir} \
	install
mv %{name}-signed.efi %{buildroot}/%{_datadir}/%{name}-%{version}/

%check
ls -la /var/run/pesign || :
%ifarch %{efi}
# for display in the build log
for x in %{buildroot}/%{_datadir}/%{name}-%{version}/%{name}-signed.* ; do
	pesign -l -i "${x}"
	# to test the actual output
	pesign -l -i "${x}" | grep -c -q "^Signing time: $(date +%%a\ %%b\ %%d,\ %%Y)$"
	pesign -l -i "${x}" | grep -c -q '^The signer.s common name is Fedora Secure Boot Signer$' ||
	pesign -l -i "${x}" | grep -c -q '^The signer.s common name is fwupd-signer$'
done
%endif

%files
%doc README COPYING
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/%{name}.efi
%{_datadir}/%{name}-%{version}/%{name}-signed*.efi

%changelog
* Wed Feb 01 2023 Robbie Harwood <rharwood@redhat.com> - 5.28
- Rise and sign

* Tue Jul 12 2022 Robbie Harwood <rharwood@redhat.com> - 5.27
- Test test app itself

* Tue Dec 08 2020 Peter Jones <pjones@redhat.com> - 5-26
- Test bkernel02

* Thu Jul 16 2020 Peter Jones <pjones@redhat.com> - 5-25
- Test pesign-113-10.fc33

* Thu Jul 16 2020 Peter Jones <pjones@redhat.com> - 5-24
- Try naming the cert differently

* Mon Jul 13 2020 Peter Jones <pjones@redhat.com> - 5-23
- Test builders again again

* Mon Jul 13 2020 Peter Jones <pjones@redhat.com> - 5-22
- Test builders again again

* Mon Jul 13 2020 Peter Jones <pjones@redhat.com> - 5-21
- Test builders again again

* Mon Jul 13 2020 Peter Jones <pjones@redhat.com> - 5-20
- Test builders again

* Tue Jul 07 2020 Peter Jones <pjones@redhat.com> - 5-19
- Make sure this still works with pesign-113-8~1.fc33

* Mon Jul 06 2020 Peter Jones <pjones@redhat.com> - 5-14
- Build again

* Thu Jun 11 2020 Peter Jones <pjones@redhat.com> - 5-13
- Rebuild to test pesign-113-2.fc33 client

* Tue Nov 12 2019 Peter Jones <pjones@redhat.com> - 5-12
- Fix gnu-efi include paths.
  Resolves: rhbz#1736420

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 15 2017 Peter Jones <pjones@redhat.com> - 5-7
- Trying an f27 build with pesign-0.112-20 on the host and in the chroot.

* Tue Aug 15 2017 Peter Jones <pjones@redhat.com> - 5-6
- Try an f27 build...

* Mon Aug 14 2017 Peter Jones <pjones@redhat.com> - 5-5
- Try this again.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 17 2016 Peter Jones <pjones@redhat.com> - 5-1
- Update to pesign-test-app-5, which adds Aarch64 support.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 17 2015 Peter Jones <pjones@redhat.com> - 0.4-14
- Right hand.

* Tue Feb 17 2015 Peter Jones <pjones@redhat.com> - 0.4-13
- Left hand.

* Mon Nov 10 2014 Peter Jones <pjones@redhat.com> - 0.4-12
- And the other shoe drops.

* Mon Nov 10 2014 Peter Jones <pjones@redhat.com> - 0.4-11
- I bet you don't know why this is getting built now.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 28 2013 Peter Jones <pjones@redhat.com> - 0.4-4
- Rebuilding to make sure bkernel01 is working right

* Wed May 22 2013 Peter Jones <pjones@redhat.com> - 0.4-2
- Add %%check

* Tue May 21 2013 Peter Jones <pjones@redhat.com> - 0.4-1
- Make it build on i686.

* Tue May 21 2013 Peter Jones <pjones@redhat.com> - 0.3-1
- First attempt.
