Name:           udiskie
Version:        2.5.8
Release:        %{autorelease}
Summary:        Removable disk auto-mounter

# SPDX
License:        MIT
URL:            https://github.com/coldfix/udiskie

Source0:        %{pypi_source udiskie}
Source1:        50-udiskie.rules

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  make asciidoc gettext

Requires:       python3-%{name} = %{version}-%{release}

Requires:       hicolor-icon-theme
Requires:       polkit

Recommends:     libnotify

%description
%{name} is a front-end for UDisks written in python. Its main purpose is
automatically mounting removable media, such as CDs or flash drives. It has
optional mount notifications, a GTK tray icon and user level CLIs for manual
mounting and unmounting operations.

%package -n python3-%{name}
Summary:        %{summary}

%description -n python3-%{name}
%{name} is a front-end for UDisks written in python. This package provides the
python 3 modules used by the %{name} binaries.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%make_build -C doc

%install
%pyproject_install
# Polkit rules
install -p -m644 -Dt ${RPM_BUILD_ROOT}%{_sysconfdir}/polkit-1/rules.d %{SOURCE1}
# Install man page and "links" for all binaries
install -p -m644 -Dt ${RPM_BUILD_ROOT}%{_mandir}/man8 doc/%{name}.8
for other in %{name}-mount %{name}-umount %{name}-info; do
    printf '.so man8/%%s.8\n' %{name} > ${RPM_BUILD_ROOT}%{_mandir}/man8/"${other}.8"
done

# Record installed files
%pyproject_save_files -l %{name}
%find_lang %{name}

%check
# test_cache.py needs python3-keyutils, which is not available
%{python3} -m unittest test.test_match

%files -f %{name}.lang
%doc README.rst
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-info
%{_bindir}/%{name}-mount
%{_bindir}/%{name}-umount
%config(noreplace)  %{_sysconfdir}/polkit-1/rules.d/50-%{name}.rules
%{_mandir}/man8/%{name}*.8*
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}*

%files -n python3-%{name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
