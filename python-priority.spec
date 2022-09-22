%global srcname priority

%global common_description %{expand:
A HTTP/2 Priority Implementation Priority is a pure-Python
implementation of the priority logic for HTTP/2, set out in RFC 7540 Section
5.3 (Stream Priority)_. This logic allows for clients to express a preference
for how the server allocates its (limited) resources to the many outstanding
HTTP requests that may be running over a single HTTP/2 connection.}

Name:           python-%{srcname}
Version:        2.0.0
Release:        %autorelease
Summary:        A pure-Python implementation of the HTTP/2 priority tree

License:        MIT
URL:            http://python-hyper.org/priority/
VCS:            https://github.com/python-hyper/priority
Source0:        %vcs/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description %{common_description}

%package -n     python3-%{srcname}
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
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=%{pyproject_build_lib} sphinx-build docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc *.rst

%files doc
%doc html
%license LICENSE

%changelog
%autochangelog
