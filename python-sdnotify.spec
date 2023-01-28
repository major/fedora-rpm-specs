Name:           python-sdnotify
Version:        0.3.2
Release:        %autorelease
License:        MIT
Summary:        A pure Python implementation of systemd's service notification protocol
URL:            https://github.com/bb4242/sdnotify
Source0:        %{pypi_source sdnotify}
BuildArch:      noarch

BuildRequires: python3-devel

Requires: systemd

%global _description %{expand:
This is a pure Python implementation of the systemd sd_notify protocol. This
protocol can be used to inform systemd about service start-up completion,
watchdog events, and other service status changes. Thus, this package can be
used to write system services in Python that play nicely with systemd. sdnotify
is compatible with both Python 2 and Python 3.
}

%description %_description

%package -n     python3-sdnotify
Summary:        %{summary}

%description -n python3-sdnotify %_description

%prep
%autosetup -n sdnotify-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sdnotify

%check
# NOTE(neil) - 2023-01-25 upstream does not provide any tests yet
%pyproject_check_import

%files -n python3-sdnotify -f %{pyproject_files}
%license LICENSE.txt

%changelog
%autochangelog

