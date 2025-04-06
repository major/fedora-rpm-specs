%global pkg async

Name:           emacs-%{pkg}
Version:        1.9.9
Release:        %autorelease
Summary:        Asynchronous processing in Emacs
License:        GPL-3.0-or-later
URL:            https://github.com/jwiegley/emacs-async
Source0:        %{url}/archive/v%{version}/%{pkg}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  emacs make
Requires:       emacs(bin)%{?_emacs_version: >= %{_emacs_version}}

%description
%{name} is a module for doing asynchronous processing in Emacs.

%prep
%autosetup

%build
%make_build

%install
# Async doesn't append the PREFIX on top of DESTDIR when DESTDIR is defined.
mkdir -p %{buildroot}/%{_emacs_sitelispdir}/%{pkg}
make DESTDIR=%{buildroot}/%{_emacs_sitelispdir}/%{pkg} install

%check
emacs --batch -L . -l async-test.el -f async-test-1 -f async-test-2 \
      -f async-test-3 -f async-test-4 -f async-test-5 -f async-test-6

%files
%doc README.md
%license COPYING
%{_emacs_sitelispdir}/%{pkg}


%changelog
%autochangelog
