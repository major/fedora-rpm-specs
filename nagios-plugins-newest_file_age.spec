%global nagiospluginsdir %{_libdir}/nagios/plugins
Name:           nagios-plugins-newest_file_age
Version:        1.1
Release:        %autorelease
Summary:        Nagios Plugin - check_newest_file_age
License:        MIT
URL:            https://exchange.nagios.org/directory/Plugins/System-Metrics/File-System/check_newest_file_age/details
Source:         https://github.com/thehunmonkgroup/nagios-plugin-newest-file-age/archive/v%{version}/%{name}-%{version}.tar.gz

Requires:       /usr/bin/sh
Requires:       coreutils

# Require the package that owns the plugins dir, as we install the plugin there.
Requires:       nagios-common

BuildRequires:  /usr/bin/install

# The package does not contain any architecture-dependent things, but installs
# into an arch-dependent directory. Thus, it cannot be noarch, but it does not
# provide any debuginfo.
%global debug_package %{nil}

%description
This plugin pulls the most recently created file in each specified directory,
and checks its created time against the current time. If the maximum age of the
file is exceeded, a warning/critical message is returned as appropriate.

%prep
%autosetup -p1 -n nagios-plugin-newest-file-age-%{version}

%build
# Nothing to do here.


%install
install -p -D -t %{buildroot}/%{nagiospluginsdir} check_newest_file_age

%files
%doc README.md
%license LICENSE
%{nagiospluginsdir}/*


%changelog
%autochangelog
