%global         srcname         mf2py
%global         forgeurl        https://github.com/microformats/mf2py
Version:        2.0.1
%global         tag             v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Microformats2 parser written in Python

License:        MIT
URL:            %{forgeurl}
Source:         %{forgeurl}/archive/%{tag}/%{srcname}-%{version}.tar.gz
# Mock is in standard library
# https://github.com/microformats/mf2py/pull/222
Patch:          mock.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildArch: noarch

%global _description %{expand:
mf2py is a Python microformats parser with full support for microformats2,
backwards-compatible support for microformats1 and experimental support for
metaformats.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version} -p 1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTORS.md
%license LICENSE

%changelog
%autochangelog
