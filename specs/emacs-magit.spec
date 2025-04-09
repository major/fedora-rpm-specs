%define pkg magit
%define pkgname Magit

Name:           emacs-%{pkg}
Version:        4.2.0
Release:        %autorelease
Summary:        Emacs interface to the most common Git operations
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://magit.vc

Source0:        https://github.com/magit/magit/archive/refs/tags/v%{version}.tar.gz
Source1:        magit-init.el

BuildArch:      noarch
BuildRequires:  emacs emacs-async emacs-dash
BuildRequires:  emacs-with-editor make texinfo git-core
BuildRequires:  emacs-transient > 0.2.0-1
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-async emacs-dash emacs-transient emacs-with-editor
Requires:       git-core
Obsoletes:      emacs-%{pkg}-el < %{version}-%{release}
Provides:       emacs-%{pkg}-el = %{version}-%{release}

%description
%{pkgname} is an add-on package for GNU Emacs. It is an interface to
the Git source-code management system that aims to make the most
common operations convenient.

%prep
%autosetup -n %{pkg}-%{version}

%global MAKE_PARMS VERSION="%{version}-%{release}" LOAD_PATH="-L %{_emacs_sitelispdir}/dash -L %{_emacs_sitelispdir}/transient -L %{_emacs_sitelispdir}/with-editor -L $(pwd)/lisp"

%build
make BUILD_MAGIT_LIBGIT=false \
    %{MAKE_PARMS} \
    versionlib lisp info

%check
# Some tests depend on a full git repository, so add a simple test here.
emacs --batch -L lisp -l %{pkg} -f %{pkg}-version 2>&1 \
    | grep "%{pkgname} %{version}"

%install
make install-lisp install-info \
    %{MAKE_PARMS} \
    DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} BUILD_MAGIT_LIBGIT=false

mkdir -p %{buildroot}%{_emacs_sitestartdir}/
cp -p %{SOURCE1} %{buildroot}%{_emacs_sitestartdir}/

%files
%license LICENSE
%doc README.md
%{_emacs_sitelispdir}/%{pkg}
%{_emacs_sitestartdir}/magit-init.el
%{_infodir}/%{pkg}*.info.*


%changelog
%autochangelog
