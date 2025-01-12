Name:      python-pathvalidate
Version:   3.2.3
Release:   %autorelease
Summary:   Library to sanitize/validate a string such as file-names/file-paths/etc

# SPDX
License:   MIT
URL:       https://github.com/thombashi/pathvalidate
Source:    %{pypi_source pathvalidate}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-allpairspy
BuildRequires:  python3-click
BuildRequires:  python3-tcolorpy

%description
%{summary}.

%package -n python3-pathvalidate
Summary:        %{summary}

%description -n python3-pathvalidate
%{summary}.

%prep
%autosetup -n pathvalidate-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files -l pathvalidate


%check
%{pytest}


%files -n python3-pathvalidate -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
