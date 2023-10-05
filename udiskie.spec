Name:           udiskie
Version:        2.5.0
Release:        %{autorelease}
Summary:        Removable disk auto-mounter

License:        MIT
URL:            https://pypi.org/project/%{name}
Source0:        %{pypi_source}
Source1:        50-udiskie.rules

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  asciidoc gettext
BuildRequires:  python3-devel python3-setuptools

# Require the module for the correct python
Requires: python3-%{name} = %{version}-%{release}

# Require package implementing required functionality
Requires: polkit hicolor-icon-theme

# Recommend tag not supported on EPEL
%if 0%{?!rhel}
# Recommended for full functionality
Recommends: libnotify
%endif

%description
%{name} is a front-end for UDisks written in python. Its main purpose is
automatically mounting removable media, such as CDs or flash drives. It has
optional mount notifications, a GTK tray icon and user level CLIs for manual
mounting and unmounting operations.

%package -n python3-%{name}
Summary: Python 3 module for udisks disk automounting
%global non_python_requires udisks2 gtk3 python3-gobject

BuildRequires: %{non_python_requires}
BuildRequires: %{py3_dist docopt PyYAML}
Requires: %{non_python_requires}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
%{name} is a front-end for UDisks written in python. This package provides the
python 3 modules used by the %{name} binaries.

%prep
%setup -q
find -name '*.txt' -exec chmod -x '{}' +
find -name '*.py' -exec sed -i 's|^#!python|#!%{__python3}|' '{}' +

# Make test folder into a proper module, if it already isn't
[ -f test/__init__.py ] || touch test/__init__.py

# Use Fedora patch for bash completions
sed -i 's|bash-completions/completions|bash-completion/completions|g' setup.py

%build
%py3_build

# Build man page
%make_build -C doc

%install
%py3_install
find %{buildroot}%{python3_sitelib} -name '*.exe' -delete

# Install polkit rules
install -p -D -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/polkit-1/rules.d/50-%{name}.rules

# Install man page
install -d %{buildroot}%{_mandir}/man8
install -p -m644 -t %{buildroot}%{_mandir}/man8 doc/%{name}.8

# Create man pages for other binaries
for other in %{name}-mount %{name}-umount %{name}-info; do
  echo ".so man8/%{name}.8" > %{buildroot}%{_mandir}/man8/"${other}.8"
done

# Find all localization files
%find_lang %{name}

%check
# Only run tests with satisfied dependencies
%{__python3} setup.py test --test-suite test.test_match

%files -f %{name}.lang
%{_mandir}/man8/%{name}*.8*
%doc README.rst
%license COPYING
%config(noreplace) %{_sysconfdir}/polkit-1/rules.d/50-%{name}.rules
%{_bindir}/%{name}
%{_bindir}/%{name}-mount
%{_bindir}/%{name}-umount
%{_bindir}/%{name}-info
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}*

%files -n python3-%{name}
%doc README.rst
%license COPYING
%{python3_sitelib}/*


%changelog
%autochangelog
