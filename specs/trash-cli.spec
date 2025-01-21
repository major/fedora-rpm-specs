Summary:        Command line interface to the freedesktop.org trashcan
Name:           trash-cli
Version:        0.24.5.26
Release:        %autorelease
License:        GPL-2.0-or-later
URL  :          https://github.com/andreafrancia/trash-cli
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:		virtualenv-versionlift.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%description
trash-cli provides a command line trash usable with GNOME, KDE, Xfce or any
freedesktop.org compatible trash implementation. The command line interface is
compatible with rm and you can use trash-put as an alias to rm.

%prep
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l trashcli

%check
# There is a tox.ini in the repo and buildrequires -t works, but the README
# instructs to run pytest, so we do that. "not slow" should be enough for
# a quick verification.
%pytest -m "not slow"

%files -f %{pyproject_files}
%doc README.rst

%{_bindir}/trash*
%{_mandir}/man1/trash*

%changelog
%autochangelog
