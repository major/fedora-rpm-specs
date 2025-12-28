Name:           python-pathlib-abc
Version:        0.5.2
Release:        %autorelease
Summary:        Backport of pathlib ABCs

License:        PSF-2.0
URL:            https://github.com/barneygale/pathlib-abc
Source:         %{pypi_source pathlib_abc}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-test
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Base classes for pathlib.Path-ish objects. This package is a preview of pathlib
functionality planned for a future release of Python; specifically, it provides
three ABCs that can be used to implement path classes for non-local
filesystems, such as archive files and storage servers: JoinablePath,
ReadablePath, and WritablePath.}

%description %_description

%package -n     python3-pathlib-abc
Summary:        %{summary}

%description -n python3-pathlib-abc %_description

%prep
%autosetup -p1 -n pathlib_abc-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pathlib_abc

%check
%pytest -ra

%files -n python3-pathlib-abc -f %{pyproject_files}
%doc README.rst CHANGES.rst

%changelog
%autochangelog
