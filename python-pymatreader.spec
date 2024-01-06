%bcond_without tests
%global debug_package   %{nil}

%global desc %{expand:
A Python module to read Matlab files. This module works with both the old (<
7.3) and the new (>= 7.3) HDF5 based format. The output should be the same for
both kinds of files.

Documentation can be found here: http://pymatreader.readthedocs.io/en/latest/}

Name:           python-pymatreader
Version:        0.0.32
Release:        %autorelease
Summary:        Convenient reader for Matlab mat files

License:        BSD
URL:            https://gitlab.com/obob/pymatreader/
Source0:        %{url}/-/archive/v%{version}/pymatreader-v%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# https://bugzilla.redhat.com/show_bug.cgi?id=2116690
ExcludeArch:    s390x

BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description %{desc}


%package -n python3-pymatreader

Summary:        %{summary}


%description -n python3-pymatreader %{desc}

%prep
%autosetup -n pymatreader-v%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l pymatreader

%check
%if %{with tests}
# Reported upstream: https://gitlab.com/obob/pymatreader/-/issues/9
%{pytest} -k "not test_files_with_unsupported_classesv7"
%endif

%files -n python3-pymatreader -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
