%global pypi_name flask-compress
%global forgeurl https://github.com/colour-science/flask-compress

%bcond tests 1

%global _description %{expand:
Flask-Compress allows you to easily compress your Flask application's
responses with gzip.

The preferred solution is to have a server (like Nginx) automatically
compress the static files for you. If you don't have that option
Flask-Compress will solve the problem for you.}

Name:           python-%{pypi_name}
Version:        1.18
Release:        %autorelease
Summary:        Compress responses in your Flask app with gzip or brotli
%forgemeta
License:        MIT
URL:            %forgeurl
Source0:        %forgesource
# Relax setuptools_scm version requirement
Patch0:         flask-compress_setuptools-scm.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(flask-caching)
%endif

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(brotli)
Requires:       python3dist(flask)
%description -n python3-%{pypi_name} %_description

%prep
%forgeautosetup -p1
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires -r

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files flask_compress

%check
%if %{with tests}
# Skip tests requiring network
%pytest -v -k 'not UrlTests'
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
