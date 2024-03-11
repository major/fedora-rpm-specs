Name:       fpaste
Version:    0.4.5.1
Release:    %autorelease
Summary:    A simple tool for pasting info onto the Fedora community paste server
BuildArch:  noarch
# spdx
License:    GPL-3.0-or-later
URL:        https://pagure.io/%{name}
Source0:    https://pagure.io/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make

Requires:    python3

%description
It is often useful to be able to easily paste text to the Fedora
Pastebin at http://paste.fedoraproject.org and this simple script
will do that and return the resulting URL so that people may
examine the output. This can hopefully help folks who are for
some reason stuck without X, working remotely, or any other
reason they may be unable to paste something into the pastebin.

This is not a general client for paste servers. It will only ever support the
paste server that the Fedora community is running.

%prep
%autosetup

%build
#nothing required

%install
mkdir -p %{buildroot}%{_bindir}
make install BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir}
install -p -m 0644 -D -T completions/bash/fpaste.bash %{buildroot}/%{bash_completions_dir}/fpaste


%files
%{_bindir}/%{name}
%doc README.rst TODO
%{_mandir}/man1/%{name}.1.gz
%{bash_completions_dir}/%{name}
%license COPYING

%changelog
%autochangelog
