import org.antlr.v4.runtime.RuleContext;

import java.io.File;
import java.io.IOException;

public class PythonParser{
    public static void main(String[]args){

        File file = new File("/home/liza/PycharmProjects/Topics in Alg/Needleman-Wunsh alg.py");
        ParserFacade parser = new ParserFacade();
        RuleContext context = null;
        AstPrinter ast_printer = new AstPrinter();
        try {
            context = parser.parse(file);
        } catch (IOException e) {
            e.printStackTrace();
        }
        if (context!=null) {
            System.out.println(context);
            ast_printer.print(context);
        }


    }
}