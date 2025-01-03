%global texpkg    cjw
%global texpkgdir %{_texmf_main}/tex/latex/%{texpkg}
%global texpkgdoc %{_texmf_main}/doc/latex/%{texpkg}

Name:             tex-cjw
Version:          20120925
Release:          %autorelease
Summary:          LaTeX class for writing resumes and cover letters
BuildArch:        noarch

License:          LPPL-1.3c
Source0:          http://tug.ctan.org/macros/latex2e/contrib/cjw.zip

BuildRequires:    /usr/bin/kpsewhich
Requires:         tex(latex)
Requires(post):   /usr/bin/texhash
Requires(postun): /usr/bin/texhash

%description
cjw is a LaTeX class for writing resumes.

%prep
%setup -q -n cjw

%build

%install
install -d -m 755 %{buildroot}%{texpkgdir}
install -p -m 644 *.{cls,sty} %{buildroot}%{texpkgdir}/

%files
%{texpkgdir}

%post
%texlive_post

%postun
%texlive_postun

%posttrans
%texlive_posttrans

%changelog
%autochangelog
