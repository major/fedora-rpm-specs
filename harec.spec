%global commit a1aa5039bc199cfe56731dcdd4e1cb616a9ab7a5
%global shortcommit %(c=%{commit}; echo ${c:0:8})
%global date 20221126

Summary:        Hare bootstrap compiler
Name:           harec
License:        GPL-3.0-only

Version:        0^%{date}git%{shortcommit}
Release:        3%{?dist}

URL:            https://git.sr.ht/~sircmpwn/harec
Source0:        %{url}/archive/%{shortcommit}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  qbe

# Due to qbe dependency 
ExclusiveArch: x86_64 aarch64

%description
This is a Hare compiler written in C11 for POSIX-compatible systems.
It is intended as a bootstrap compiler and using the Hare standard
library is recommended for production use.

%prep
%autosetup -n %{name}-%{shortcommit}

%build
# Note: we do not use the configure macro since it set some flags 
# which are not supported by upstream's script.
./configure \
  --prefix=%{_prefix} \
  --bindir=%{_bindir} \
  --sysconfdir=%{_sysconfdir} \
  --libdir=%{_libdir} \
  --mandir=%{_mandir}
%make_build

%install
%make_install

%check
make check

%files
%license COPYING
%doc README.md
%doc docs/declaration_solver.txt
%doc docs/env.txt
%doc docs/runtime.txt
%{_bindir}/harec

%changelog
* Thu Dec 22 2022 Benson Muite <benson_muite@emailplus.org> - 0^20221126gita1aa5039-3
- Move configure to build section

* Mon Dec 19 2022 Benson Muite <benson_muite@emailplus.org> - 0^20221126gita1aa5039-2
- Update build flags and versioning based on review

* Fri Dec 16 2022 Benson Muite <benson_muite@emailplus.org> - 0^20221126gita1aa5039-1
- Initial packaging

