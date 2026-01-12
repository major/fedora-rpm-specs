Name:           datamash
Version:        1.9
Release:        %autorelease
Summary:        A statistical, numerical and textual operations tool

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/%{name}/
# upstream signed 1.9 release with public key: 33382C8D62017A1012A05B35BDB72EC3D3F87EE6
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz


BuildRequires:  gcc
# required by the testsuite under tests/
BuildRequires:  gettext perl(Digest::MD5) perl(Digest::SHA) perl(Data::Dumper)
BuildRequires:  perl(FileHandle) perl(File::Compare) perl(File::Find)
# required by tests/datamash-vnlog.pl
BuildRequires:  perl(lib)
BuildRequires:  pkgconfig bash-completion
BuildRequires:  make
BuildRequires:  texinfo


%description
GNU datamash is a command-line program which performs basic
numeric,textual and statistical operations on input textual data
files.


%prep
%autosetup -p1


%build
%configure
%make_build


%install
%make_install
%{__rm} -f %{buildroot}/%{_infodir}/dir
%find_lang %{name}
%{__mkdir_p} %{buildroot}%{bash_completions_dir}
%{__mv} %{buildroot}%{_datadir}/datamash/bash-completion.d/datamash %{buildroot}%{bash_completions_dir}
# E: non-executable-script /usr/share/bash-completion/completions/datamash 644 /bin/bash
%{__sed} -i '/^#!/,1d' %{buildroot}%{bash_completions_dir}/datamash


%check
%{__make} check || { echo 'begin test-suite.log'; cat test-suite.log; echo 'end test-suite.log'; false; }


%files -f %{name}.lang
%{_bindir}/*
%{_datadir}/datamash/
%{_infodir}/datamash.info.*
%{bash_completions_dir}/datamash


%license COPYING
%doc README NEWS THANKS AUTHORS ChangeLog
%{_mandir}/man1/*


%changelog
%autochangelog
