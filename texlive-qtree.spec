# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/qtree
# catalog-date 2009-01-24 16:10:54 +0100
# catalog-license lppl
# catalog-version 3.1b
Name:		texlive-qtree
Version:	3.1b
Release:	10
Summary:	Draw tree structures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/qtree
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qtree.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qtree.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.1b-2
+ Revision: 755569
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.1b-1
+ Revision: 719424
- texlive-qtree
- texlive-qtree
- texlive-qtree
- texlive-qtree

