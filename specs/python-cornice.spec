%global pypi_name cornice
%global desc Helpers to build & document Web Services with Pyramid.

Name:             python-cornice
Version:          6.1.0
Release:          %autorelease
BuildArch:        noarch

License:          MPL-2.0
Summary:          Define Web Services in Pyramid
URL:              https://github.com/Cornices/cornice/
Source:           %{pypi_source cornice}

BuildRequires: python3-devel

# For tests
BuildRequires: %{py3_dist pytest}
BuildRequires: %{py3_dist colander}
BuildRequires: %{py3_dist marshmallow}
BuildRequires: %{py3_dist webtest}

%description
%{desc}


%package -n python3-cornice
Summary:          %{summary}

Recommends: %{py3_dist colander}

%description -n python3-%{pypi_name}
%{desc}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%pytest -v


%files -n python3-cornice -f %{pyproject_files}
%doc CHANGES.txt CONTRIBUTORS.txt README.rst


%changelog
%autochangelog
