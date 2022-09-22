
%global srcname imageio

Name: python-%{srcname}
Version: 2.9.0
Release: 6%{?dist}
Summary: Python IO of image, video, scientific, and volumetric data formats.
License: BSD
URL: https://imageio.github.io
Source0: %{pypi_source}

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
# testing
# BuildRequires: python3-pytest
# BuildRequires: python3-numpy

%description
Imageio is a Python library that provides an easy interface to read and write a wide range of image data, including animated images, volumetric data, and scientific formats.

%package -n python3-%{srcname}
Summary: Python IO of image, video, scientific, and volumetric data formats.
BuildRequires: python3-devel python3-setuptools

%description -n python3-%{srcname}
Imageio is a Python library that provides an easy interface to read and write a wide range of image data, including animated images, volumetric data, and scientific formats.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

# Testing requires image sample, either local or from the internet
# %%check 
# export IMAGEIO_NO_INTERNET="1"
# %%pytest  --ignore=tests/test_ffmpeg.py  --ignore=tests/test_ffmpeg_info.py tests/

%files -n python3-%{srcname}
%doc README.md
%license LICENSE
# Downloads binary freeimage library
%exclude %{_bindir}/imageio*
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-*.egg-info

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.9.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.9.0-2
- Rebuilt for Python 3.10

* Wed Feb 03 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 2.9.0-1
- Initial package

