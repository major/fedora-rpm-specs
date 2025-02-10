Name:           git2cl
Version:        3.0
Release:        %autorelease
Summary:        Converts git logs to GNU style ChangeLog format

License:        GPL-2.0-or-later
URL:            https://savannah.nongnu.org/projects/git2cl

Source0:        https://git.savannah.gnu.org/cgit/git2cl.git/snapshot/git2cl-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators

Requires:       git

%description
A quick tool to convert git logs to GNU ChangeLog format.

The tool invokes git log internally unless you pipe a log to it. 

%prep
%autosetup -n git2cl-%{version}

%build
# Nothing to build.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 git2cl $RPM_BUILD_ROOT%{_bindir}/git2cl

%files
%{_bindir}/git2cl
%doc README.md 
%license COPYING

%changelog
%autochangelog
