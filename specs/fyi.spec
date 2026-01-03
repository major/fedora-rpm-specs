Name:           fyi
Version:        1.0.4
Release:        %autorelease
Summary:        Command line utility to send desktop notifications
License:        MIT
URL:            https://codeberg.org/dnkl/fyi
Source:         https://codeberg.org/dnkl/%{name}/archive/%{version}.tar.gz

Patch0:		fyi-no-const.patch

BuildRequires:  dbus-devel
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  scdoc

%description
FYI (for your information) is a command line utility to send desktop
notifications to the user via a notification daemon implementing XDG desktop
notifications.


%package bash-completion
Summary: Bash completion files for %{name}
Requires: bash-completion
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description bash-completion
%{summary}


%package fish-completion
Summary: Fish completion files for %{name}
Requires: fish
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description fish-completion
%{summary}

%prep
%autosetup -p1 -n %{name}

%build
%meson
%meson_build

%install
%meson_install
rm -r %{buildroot}/%{_datadir}/doc/%{name}/

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files fish-completion
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%changelog
%autochangelog
