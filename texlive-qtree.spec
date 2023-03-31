Name:		texlive-qtree
Version:	15878
Release:	2
Summary:	Draw tree structures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/qtree
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qtree.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qtree.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers support for drawing tree diagrams, and is
especially suitable for linguistics use. It allows trees to be
specified in a simple bracket notation, automatically
calculates branch sizes, and supports both DVI/PostScript and
PDF output by use of pict2e facilities. The package is a
development of the existing qobitree package, offering a new
front end.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/qtree/qtree.sty
%doc %{_texmfdistdir}/doc/latex/qtree/README
%doc %{_texmfdistdir}/doc/latex/qtree/qarrows.pdf
%doc %{_texmfdistdir}/doc/latex/qtree/qarrows.tex
%doc %{_texmfdistdir}/doc/latex/qtree/qtreenotes.pdf
%doc %{_texmfdistdir}/doc/latex/qtree/qtreenotes.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
