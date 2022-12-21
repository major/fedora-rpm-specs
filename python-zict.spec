%global srcname zict

Name:           python-%{srcname}
Version:        2.2.0
Release:        %autorelease
Summary:        Mutable mapping tools

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(lmdb)
BuildRequires:  python3dist(psutil)

%global _description %{expand:
Zict builds abstract MutableMapping classes that consume and build on other
MutableMappings. They can be composed with each other to form intuitive
interfaces over complex storage systems policies.

Data can be stored in-memory, on disk, in archive files, etc., managed with
different policies like LRU, and transformed when arriving or departing the
dictionary.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{pytest} -ra

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
