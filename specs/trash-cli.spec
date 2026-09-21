Summary:        Command line interface to the freedesktop.org trashcan
Name:           trash-cli
Version:        0.26.9.14
Release:        %autorelease
License:        GPL-2.0-or-later
URL  :          https://github.com/andreafrancia/trash-cli
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%description
trash-cli provides a command line trash usable with GNOME, KDE, Xfce or any
freedesktop.org compatible trash implementation. The command line interface is
compatible with rm and you can use trash-put as an alias to rm.

%prep
%autosetup -n %{name}-%{version} -p1
# clean specific requirements for older (eol) python versions
# this removes the whole line if it matches in any combination
sed -i -E "/; python_version (~=|<) '(2.7|3.4|3.3|3.5|3.8)'/d" setup.cfg

%generate_buildrequires
%pyproject_buildrequires -x dev

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l trashcli

%check
# There is a tox.ini in the repo, but the README instructs to run pytest.
# "not slow" should be enough for a quick verification.
%pytest -m "not slow"

%files -f %{pyproject_files}
%doc README.rst

%{_bindir}/trash*
%{_mandir}/man1/trash*

%changelog
%autochangelog
