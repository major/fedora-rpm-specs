Name:           gnome-shell-rpm-generators
Version:        1
Release:        %autorelease
Summary:        RPM generators for gnome-shell

License:        MIT
URL:            https://src.fedoraproject.org/rpms/gnome-shell-rpm-generators
Source:         LICENSE
Source:         gnome_shell.attr
Source:         gnome_shell_requires.sh

BuildArch:      noarch

Requires:       jq

%description
RPM generators for gnome-shell.

Currently it generates:

```
Provides: gnome-shell-extension(UUID)
Requires: (gnome-shell(api) = VER1 or gnome-shell(api) = VER2 or ...)
```

%prep
%autosetup -c -T
cp -a %{sources} .


%build


%install
install -Dpm0644 -t %{buildroot}%{_fileattrsdir} *.attr
install -Dpm0755 -t %{buildroot}%{_rpmconfigdir} *.sh


%files
%license LICENSE
%{_fileattrsdir}/gnome_shell.attr
%{_rpmconfigdir}/gnome_shell_requires.sh


%changelog
%autochangelog

