Name:           python-pyinotify
Version:        0.9.6
Release:        %autorelease
Summary:        Linux filesystem events monitoring

License:        MIT
URL:            http://github.com/seb-m/pyinotify
Source:         %{pypi_source pyinotify}
BuildArch:      noarch

BuildRequires:  python3-devel
# This module was removed from Python 3.12 but was
# available as a core python module before then
BuildRequires:  python3dist(pyasyncore)
Requires:       python3dist(pyasyncore)

%global _description %{expand:
Monitoring filesystems events with inotify on Linux.}

%description %_description

%package -n     python3-pyinotify
Summary:        %{summary}

%description -n python3-pyinotify %_description


%prep
%autosetup -p1 -n pyinotify-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L pyinotify


%check
%pyproject_check_import


%files -n python3-pyinotify -f %{pyproject_files}
%license COPYING
%doc README.md

%changelog
%autochangelog
