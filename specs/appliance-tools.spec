%global __python %{__python3}

# Minimum version of imgcreate (livecd-tools)
%global min_imgcreate_ver 28.3-3

%if 0%{?fedora}
%global min_imgcreate_evr 1:%{min_imgcreate_ver}
%else
%global min_imgcreate_evr %{min_imgcreate_ver}
%endif

Name:       appliance-tools
Summary:    Tools for building Appliances
Version:    011.3
Release:    6%{?dist}
License:    GPL-2.0-only
URL:        https://pagure.io/appliance-tools
BuildArch:  noarch

Source0:    https://releases.pagure.org/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  perl-podlators
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  which

# Ensure system deps are installed (rhbz#1409536)
Requires:   curl
Requires:   kpartx
Requires:   python3-imgcreate %{?min_imgcrate_evr:>= %{min_imgcreate_evr}}
Requires:   python3-progress
Requires:   python3-setuptools
Requires:   qemu-img
Requires:   rsync
Requires:   sssd-client
Requires:   xfsprogs
Requires:   xz
Requires:   zlib

%if 0%{?fedora}
Requires:   btrfs-progs
%endif

%description
Tools for generating appliance images on Fedora based systems, including
derived distributions such as RHEL, CentOS, and others.

%prep
%autosetup -p1

%install
%make_install PYTHON=%{__python}

# Delete docs, we'll grab them later
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%files
%doc README
%doc config/fedora-aos.ks
%license COPYING
%{_mandir}/man*/*
%{_bindir}/appliance-creator
%{_bindir}/ec2-converter
%{python_sitelib}/appcreate/
%{python_sitelib}/ec2convert/

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 011.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jul 04 2025 Simone Caronni <negativo17@gmail.com> - 011.3-5
- Remove all EL7 / Python 2 conditionals.
- Trim changelog.
- Format SPEC file and sort all Requires/BuildRequires.

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 011.3-4
- Rebuilt for Python 3.14

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 011.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 011.3-2
- convert license to SPDX

* Fri Jul 26 2024 Neal Gompa <ngompa@fedoraproject.org> - 011.3-1
- Update to 011.3 release

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 011.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 011.2-8
- Rebuilt for Python 3.13

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 011.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 011.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Aug 13 2023 Neal Gompa <ngompa@fedoraproject.org> - 011.2-5
- Add runtime dep for setuptools (#2135410)

* Sun Aug 13 2023 Neal Gompa <ngompa@fedoraproject.org> - 011.2-4
- Add BR for setuptools (#2135410)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 011.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 011.2-2
- Rebuilt for Python 3.12

* Mon Jun 26 2023 Neal Gompa <ngompa@fedoraproject.org> - 011.2-1
- Update to 011.2 release

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 011.1-11
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 011.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild
