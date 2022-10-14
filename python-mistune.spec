%global srcname mistune

%global common_description %{expand:
The fastest markdown parser in pure Python, inspired by marked.}

Name:           python-mistune
Version:        2.0.4
Release:        %autorelease
Summary:        Markdown parser for Python

License:        BSD
URL:            https://github.com/lepture/mistune
Source0:        %url/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# Upstream uses tox to call nose. Instead, we'll just call pytest directly.
BuildRequires:  python3dist(pytest)

%description %{common_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}

%package doc
Summary:        Documentation for %{name}

%description doc
%{common_description}

This is the documentation package for %{name}.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires requirements-docs.txt

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=%{pyproject_build_lib} sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%{_fixperms} %{buildroot}/*

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%files doc
%doc html
%license LICENSE

%changelog
%autochangelog
