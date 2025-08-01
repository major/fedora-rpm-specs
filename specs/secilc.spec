%global libsepolver 3.9-1

Name:           secilc
Version:        3.9
Release:        2%{?dist}
Summary:        The SELinux CIL Compiler

License:        BSD-2-Clause
URL:            https://github.com/SELinuxProject/selinux/wiki
Source0:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/secilc-%{version}.tar.gz
Source1:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/secilc-%{version}.tar.gz.asc
Source2:        https://github.com/bachradsusi.gpg
# fedora-selinux/selinux: git format-patch -N 3.9 -- secilc
# i=1; for j in 00*patch; do printf "Patch%04d: %s\n" $i $j; i=$((i+1));done
# Patch list start
# Patch list end
Requires:       libsepol >= %{libsepolver}
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libsepol-static >= %{libsepolver}, dblatex, flex, xmlto, pandoc-pdf, texlive-mdwtools
BuildRequires:  gnupg2

%description
The SELinux CIL Compiler is a compiler that converts the CIL language as
described on the CIL design wiki into a kernel binary policy file.
Please see the CIL Design Wiki at:
http://github.com/SELinuxProject/cil/wiki/
for more information about the goals and features on the CIL language.

%package doc
Summary:        Documentation for the SELinux CIL Compiler
BuildArch:      noarch

%description doc
The SELinux CIL Compiler is a compiler that converts the CIL language as
described on the CIL design wiki into a kernel binary policy file.
Please see the CIL Design Wiki at:
http://github.com/SELinuxProject/cil/wiki/
for more information about the goals and features on the CIL language.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p 2 -n secilc-%{version}


%build
%set_build_flags
make %{?_smp_mflags} LIBSEPOL_STATIC=%{_libdir}/libsepol.a
pushd docs
make %{?_smp_mflags}
popd


%install
make %{?_smp_mflags} DESTDIR="%{buildroot}" SBINDIR="%{buildroot}%{_sbindir}" LIBDIR="%{buildroot}%{_libdir}" install


%files
%{_bindir}/secilc
%{_bindir}/secil2conf
%{_bindir}/secil2tree
%{_mandir}/man8/secilc.8.gz
%{_mandir}/man8/secil2conf.8.gz
%{_mandir}/man8/secil2tree.8.gz
%license LICENSE

%files doc
%doc docs/html
%doc docs/pdf
%license LICENSE

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

%autochangelog
