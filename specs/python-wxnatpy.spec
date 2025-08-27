%global desc %{expand: \
wxnatpy is a wxPython widget which allows users to browse the contents of a
XNAT repository.  It is built on top of wxPython and xnatpy.}

Name:           python-wxnatpy
Version:        0.4.0
Release:        %autorelease
Summary:        wxnatpy is a wxPython widget which allows users to browse the contents of a XNAT repository
License:        Apache-2.0
URL:            https://github.com/pauldmccarthy/wxnatpy
Source0:        %{url}/archive/%{version}/wxnatpy-%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}

%package -n python3-wxnatpy
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-wxnatpy
%{desc}

%prep
%autosetup -n wxnatpy-%{version}

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l wxnat

%check
%pyproject_check_import

%files -n python3-wxnatpy -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
