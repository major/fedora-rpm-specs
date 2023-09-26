Name:           python-pygdbmi
Version:        0.11.0.0
Release:        %autorelease
Summary:        Get Structured Output from GDB's Machine Interface 
License:        MIT
URL:            https://github.com/cs01/pygdbmi
Source0:        %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pytest
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gdb

%global _description \
GDB/MI is a line based machine oriented \
text interface to GDB and is activated by \
specifying using the --interpreter command \
line option (see Mode Options). It is\
specifically intended to support the development\
of systems which use the debugger as just one\
small component of a larger system.


%description %{_description}


%package -n python3-pygdbmi
Summary:        %{summary}


%description -n python3-pygdbmi %{_description}


%prep
%autosetup -n pygdbmi-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pygdbmi

%check
%pytest

%files -n python3-pygdbmi -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
